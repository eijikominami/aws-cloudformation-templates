"""
Unit tests for GA4 Visual ETL Lambda.

Validates:
- handle_update includes CodeGenConfigurationNodes in job_update (Bug #5 fix)
- generate_visual_etl_nodes includes SchemaChangePolicy (Bug #1 fix)
- handle_update --conf contains glue_catalog full settings

Requirements: 2.1, 2.5, 1.5
"""

import sys
from pathlib import Path
from unittest.mock import patch
import importlib

import pytest

# Ensure ga-etl-handler/app.py is loaded (not cloudfront-etl-handler/app.py)
_ga_dir = str(Path(__file__).parent.parent.parent / "src" / "lambda-functions" / "ga-etl-handler")
# Remove any previously cached 'app' module
sys.modules.pop("app", None)
sys.modules.pop("cfnresponse", None)
sys.path.insert(0, _ga_dir)
import app  # noqa: E402
importlib.reload(app)
sys.path.remove(_ga_dir)

import app  # noqa: E402


GLUE_CATALOG_REQUIRED_SETTINGS = [
    "spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog",
    "spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog",
    "spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO",
    "spark.sql.catalog.glue_catalog.warehouse=s3://",
]


class TestGenerateVisualEtlNodes:
    """generate_visual_etl_nodes must produce S3CatalogTarget with SchemaChangePolicy."""

    def test_target_node_has_schema_change_policy(self):
        """Bug #1: ターゲットノードに SchemaChangePolicy が含まれること."""
        nodes = app.generate_visual_etl_nodes(
            connection_name="ga4-connection",
            iceberg_data_bucket="iceberg-bucket",
            database_name="analytics_db",
            account_id="123456",
            source_table_name="ga_core_reports_iceberg",
        )

        target = nodes["node-target"]["S3CatalogTarget"]
        assert "SchemaChangePolicy" in target
        assert target["SchemaChangePolicy"]["EnableUpdateCatalog"] is True
        assert target["SchemaChangePolicy"]["UpdateBehavior"] == "UPDATE_IN_DATABASE"

    def test_target_node_is_s3_catalog_target(self):
        """ターゲットノードが S3CatalogTarget 型であること."""
        nodes = app.generate_visual_etl_nodes(
            "conn", "bucket", "db", "acct", "table"
        )
        assert "S3CatalogTarget" in nodes["node-target"]

    def test_source_node_has_connector_data_source(self):
        """ソースノードが ConnectorDataSource 型であること."""
        nodes = app.generate_visual_etl_nodes(
            "conn", "bucket", "db", "acct", "table"
        )
        assert "ConnectorDataSource" in nodes["node-source"]


class TestHandleUpdateCodeGenConfigurationNodes:
    """Bug #5: handle_update must include CodeGenConfigurationNodes in job_update."""

    @patch.object(app, "glue_client")
    @patch.object(app, "wait_for_job_ready", return_value="arn:aws:glue:*:*:job/test")
    def test_job_update_contains_code_gen_nodes(self, mock_wait, mock_glue):
        """handle_update の job_update に CodeGenConfigurationNodes キーが含まれること."""
        mock_glue.get_job.return_value = {
            "Job": {
                "Command": {"Name": "glueetl", "ScriptLocation": "s3://scripts/job.py", "PythonVersion": "3"},
                "DefaultArguments": {"--enable-metrics": "true"},
            }
        }
        mock_glue.update_job.return_value = {}

        app.handle_update(
            job_name="test-ga4-job",
            connection_name="ga4-connection",
            iceberg_data_bucket="iceberg-bucket",
            database_name="analytics_db",
            scripts_bucket="scripts-bucket",
            logical_name="analytics",
            iam_role_arn="arn:aws:iam::123456789012:role/GlueRole",
            account_id="123456",
            source_table_name="ga_core_reports_iceberg",
            git_repository="",
            git_owner="",
            git_branch="main",
            git_folder="glue-jobs",
            git_token="",
        )

        call_kwargs = mock_glue.update_job.call_args.kwargs
        job_update = call_kwargs["JobUpdate"]
        assert "CodeGenConfigurationNodes" in job_update, \
            "handle_update job_update must contain CodeGenConfigurationNodes"

    @patch.object(app, "glue_client")
    @patch.object(app, "wait_for_job_ready", return_value="arn:aws:glue:*:*:job/test")
    def test_job_update_nodes_have_schema_change_policy(self, mock_wait, mock_glue):
        """handle_update のノードに SchemaChangePolicy が含まれること."""
        mock_glue.get_job.return_value = {
            "Job": {
                "Command": {"Name": "glueetl", "ScriptLocation": "s3://scripts/job.py", "PythonVersion": "3"},
                "DefaultArguments": {"--enable-metrics": "true"},
                "CodeGenConfigurationNodes": {
                    "node-target": {
                        "S3CatalogTarget": {
                            "Name": "Amazon S3 (Iceberg)",
                            "Inputs": ["node-source"],
                            "Table": "ga_core_reports_iceberg",
                            "Database": "analytics_db",
                            "PartitionKeys": [],
                        }
                    }
                },
            }
        }
        mock_glue.update_job.return_value = {}

        app.handle_update(
            job_name="test-ga4-job",
            connection_name="ga4-connection",
            iceberg_data_bucket="iceberg-bucket",
            database_name="analytics_db",
            scripts_bucket="scripts-bucket",
            logical_name="analytics",
            iam_role_arn="arn:aws:iam::123456789012:role/GlueRole",
            account_id="123456",
            source_table_name="ga_core_reports_iceberg",
            git_repository="",
            git_owner="",
            git_branch="main",
            git_folder="glue-jobs",
            git_token="",
        )

        call_kwargs = mock_glue.update_job.call_args.kwargs
        nodes = call_kwargs["JobUpdate"]["CodeGenConfigurationNodes"]
        target = nodes["node-target"]["S3CatalogTarget"]
        assert target["SchemaChangePolicy"]["EnableUpdateCatalog"] is True


class TestHandleUpdateConf:
    """handle_update --conf must contain glue_catalog full settings."""

    @patch.object(app, "glue_client")
    @patch.object(app, "wait_for_job_ready", return_value="arn:aws:glue:*:*:job/test")
    def test_conf_has_glue_catalog_full_config(self, mock_wait, mock_glue):
        """handle_update の --conf に glue_catalog 4設定を含む."""
        mock_glue.get_job.return_value = {
            "Job": {
                "Command": {"Name": "glueetl", "ScriptLocation": "s3://scripts/job.py", "PythonVersion": "3"},
                "DefaultArguments": {"--enable-metrics": "true"},
            }
        }
        mock_glue.update_job.return_value = {}

        app.handle_update(
            job_name="test-ga4-job",
            connection_name="ga4-connection",
            iceberg_data_bucket="iceberg-bucket",
            database_name="analytics_db",
            scripts_bucket="scripts-bucket",
            logical_name="analytics",
            iam_role_arn="arn:aws:iam::123456789012:role/GlueRole",
            account_id="123456",
            source_table_name="ga_core_reports_iceberg",
            git_repository="",
            git_owner="",
            git_branch="main",
            git_folder="glue-jobs",
            git_token="",
        )

        call_kwargs = mock_glue.update_job.call_args.kwargs
        conf_value = call_kwargs["JobUpdate"]["DefaultArguments"]["--conf"]

        for setting in GLUE_CATALOG_REQUIRED_SETTINGS:
            assert setting in conf_value, f"handle_update --conf missing: {setting}"
