import sys
from datetime import datetime, timedelta, timezone

import boto3
from botocore.exceptions import ClientError
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.types import (LongType, StringType, StructField, StructType)
from awsglue.context import GlueContext
from awsglue.job import Job

REQUIRED = ["JOB_NAME", "SOURCE_PATH", "DATABASE_NAME", "TABLE_NAME"]
OPTIONAL = ["LOOKBACK_DAYS", "BATCH_DAYS"]

args = getResolvedOptions(sys.argv, REQUIRED + [o for o in OPTIONAL if f"--{o}" in sys.argv])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

lookback_days = int(args.get("LOOKBACK_DAYS", "3"))
batch_days = max(1, int(args.get("BATCH_DAYS", "7")))
source_paths = [p.strip().rstrip("/") + "/" for p in args["SOURCE_PATH"].split(",") if p.strip()]
table_name = f"glue_catalog.{args['DATABASE_NAME']}.{args['TABLE_NAME']}"

s3 = boto3.client("s3")
glue = boto3.client("glue")

# Declared rather than inferred, because inferring reads every file a second time
REQUESTS = StructType([
    StructField("_2xx", LongType()),
    StructField("_3xx", LongType()),
    StructField("_4xx", LongType()),
    StructField("_5xx", LongType()),
    StructField("failed", LongType()),
])

READ_SCHEMA = StructType([
    StructField("canaryName", StringType()),
    StructField("startTime", StringType()),
    StructField("endTime", StringType()),
    StructField("executionStatus", StringType()),
    StructField("executionError", StringType()),
    StructField("timeSpentInLaunchInMs", LongType()),
    StructField("timeSpentInResetInMs", LongType()),
    StructField("timeSpentInSetupInMs", LongType()),
    StructField("customerScript", StructType([
        StructField("status", StringType()),
        StructField("failureReason", StringType()),
        StructField("startTime", StringType()),
        StructField("endTime", StringType()),
        StructField("requests", REQUESTS),
    ])),
])

# S3 Tables cannot expose a table whose definition contains capitals
COLUMNS = [
    "canaryName AS canaryname",
    "startTime AS starttime",
    "endTime AS endtime",
    "executionStatus AS executionstatus",
    "executionError AS executionerror",
    "timeSpentInLaunchInMs AS timespentinlaunchinms",
    "timeSpentInResetInMs AS timespentinresetinms",
    "timeSpentInSetupInMs AS timespentinsetupinms",
    "customerScript.status AS script_status",
    "customerScript.failureReason AS script_failurereason",
    "customerScript.startTime AS script_starttime",
    "customerScript.endTime AS script_endtime",
    "customerScript.requests._2xx AS requests_2xx",
    "customerScript.requests._3xx AS requests_3xx",
    "customerScript.requests._4xx AS requests_4xx",
    "customerScript.requests._5xx AS requests_5xx",
    "customerScript.requests.failed AS requests_failed",
]


def split_uri(uri):
    bucket, _, prefix = uri[len("s3://"):].partition("/")
    return bucket, prefix


def child_prefixes(bucket, prefix):
    """One level of folders below a prefix."""
    out = []
    token = None
    while True:
        kwargs = {"Bucket": bucket, "Prefix": prefix, "Delimiter": "/"}
        if token:
            kwargs["ContinuationToken"] = token
        page = s3.list_objects_v2(**kwargs)
        out += [p["Prefix"] for p in page.get("CommonPrefixes", [])]
        token = page.get("NextContinuationToken")
        if not token:
            return out


def canary_prefixes(uri):
    """The <region>/<canary>/ folders under a source path.

    Synthetics nests each run under <prefix>/<region>/<canary>/YYYY/MM/DD/, so the
    two levels are read back from S3 instead of hard-coding that depth.
    """
    bucket, prefix = split_uri(uri)
    leaves = [prefix]
    for _ in range(2):
        nxt = []
        for p in leaves:
            nxt += child_prefixes(bucket, p)
        if not nxt:
            return bucket, []
        leaves = nxt
    return bucket, leaves


# Resolve the Canary folders once; the batches below only vary by date.
canaries = [canary_prefixes(uri) for uri in source_paths]


def paths_for(days):
    """Existing date folders for the given dates."""
    found = []
    for bucket, leaves in canaries:
        for leaf in leaves:
            for day in days:
                candidate = f"{leaf}{day.strftime('%Y/%m/%d/')}"
                if s3.list_objects_v2(Bucket=bucket, Prefix=candidate,
                                      MaxKeys=1).get("KeyCount"):
                    found.append(f"s3://{bucket}/{candidate}")
    return found


def table_exists():
    try:
        spark.table(table_name)
        return True
    except Exception:
        return False


def drop_stale_registration():
    """Remove a catalog entry whose Iceberg metadata file is gone from S3.

    Catalog-only, so the broken metadata_location is never read.
    """
    try:
        glue.delete_table(DatabaseName=args["DATABASE_NAME"], Name=args["TABLE_NAME"])
    except ClientError as ce:
        if ce.response["Error"]["Code"] != "EntityNotFoundException":
            raise


def read(paths):
    # Each report is one pretty-printed JSON object per file, so multiline is required
    df = spark.read.option("recursiveFileLookup", "true") \
        .option("pathGlobFilter", "SyntheticsReport-*.json") \
        .option("multiline", "true") \
        .schema(READ_SCHEMA) \
        .json(paths)
    return df.selectExpr(*COLUMNS)


today = datetime.now(timezone.utc).date()
wanted = [today - timedelta(days=d) for d in range(lookback_days)]
batches = [wanted[i:i + batch_days] for i in range(0, len(wanted), batch_days)]

exists = table_exists()
loaded = 0

for batch in batches:
    paths = paths_for(batch)
    if not paths:
        continue

    df = read(paths)

    if not exists:
        try:
            df.writeTo(table_name).using("iceberg").create()
        except Exception as e:
            if "already exists" in str(e).lower():
                drop_stale_registration()
                df.writeTo(table_name).using("iceberg").create()
            else:
                raise
        exists = True
    else:
        df.createOrReplaceTempView("incoming")
        # A Canary run is identified by its name and start time
        spark.sql(f"""
            MERGE INTO {table_name} AS t
            USING incoming AS s
            ON t.canaryname = s.canaryname AND t.starttime = s.starttime
            WHEN NOT MATCHED THEN INSERT *
        """)

    loaded += len(paths)

print(f"loaded {loaded} date folder(s) across {len(batches)} batch(es)")
job.commit()
