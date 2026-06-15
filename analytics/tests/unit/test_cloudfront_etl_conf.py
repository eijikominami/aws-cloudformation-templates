"""
Unit and property-based tests for CloudFront ETL Lambda --conf configuration.

Validates that handle_create and handle_update include all 4 glue_catalog
settings in DefaultArguments.--conf (Bug #2 fix verification).

Requirements: 2.2, 3.1
"""

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Add the Lambda source to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src" / "lambda-functions" / "cloudfront-etl-handler"))

import app  # noqa: E402


GLUE_CATALOG_REQUIRED_SETTINGS = [
    "spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog",
    "spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog",
    "spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO",
    "spark.sql.catalog.glue_catalog.warehouse=s3://",
]


class TestConfContainsGlueCatalogFullConfig:
    """Property: --conf MUST contain all 4 glue_catalog settings."""

    @patch.object(app, "glue_client")
    @patch.object(app, "wait_for_job_ready", return_value="arn:aws:glue:*:*:job/test")
    def test_handle_create_conf_has_glue_catalog(self, mock_wait, mock_glue):
        """handle_create の DefaultArguments.--conf に glue_catalog 4設定を含む."""
        mock_glue.create_job.return_value = {}

        app.handle_create(
            job_name="test-cf-job",
            raw_data_bucket="raw-bucket",
            access_log_prefix="logs/",
            iceberg_data_bucket="iceberg-bucket",
            database_name="analytics_db",
            target_table_name="cf_table",
            scripts_bucket="scripts-bucket",
            logical_name="analytics",
            iam_role_arn="arn:aws:iam::123456789012:role/GlueRole",
            git_repository="",
            git_owner="",
            git_branch="main",
            git_folder="glue-jobs",
            git_token="",
        )

        call_kwargs = mock_glue.create_job.call_args.kwargs
        conf_value = call_kwargs["DefaultArguments"]["--conf"]

        for setting in GLUE_CATALOG_REQUIRED_SETTINGS:
            assert setting in conf_value, f"handle_create --conf missing: {setting}"

    @patch.object(app, "glue_client")
    @patch.object(app, "wait_for_job_ready", return_value="arn:aws:glue:*:*:job/test")
    def test_handle_update_conf_has_glue_catalog(self, mock_wait, mock_glue):
        """handle_update の DefaultArguments.--conf に glue_catalog 4設定を含む."""
        mock_glue.get_job.return_value = {
            "Job": {
                "Command": {"Name": "glueetl", "ScriptLocation": "s3://scripts/job.py", "PythonVersion": "3"},
                "DefaultArguments": {"--enable-metrics": "true"},
            }
        }
        mock_glue.update_job.return_value = {}

        app.handle_update(
            job_name="test-cf-job",
            raw_data_bucket="raw-bucket",
            access_log_prefix="logs/",
            iceberg_data_bucket="iceberg-bucket",
            database_name="analytics_db",
            target_table_name="cf_table",
            scripts_bucket="scripts-bucket",
            logical_name="analytics",
            iam_role_arn="arn:aws:iam::123456789012:role/GlueRole",
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

    @pytest.mark.parametrize("bucket_name", [
        "my-iceberg-bucket",
        "analytics-iceberg-data-ap-northeast-1-857135586997",
        "bucket-with-special.chars-123",
    ])
    @patch.object(app, "glue_client")
    @patch.object(app, "wait_for_job_ready", return_value="arn:aws:glue:*:*:job/test")
    def test_handle_create_warehouse_uses_iceberg_data_bucket(self, mock_wait, mock_glue, bucket_name):
        """Property: warehouse は常に s3://{iceberg_data_bucket}/iceberg-warehouse/ を使用."""
        mock_glue.create_job.return_value = {}

        app.handle_create(
            job_name="test-cf-job",
            raw_data_bucket="raw-bucket",
            access_log_prefix="logs/",
            iceberg_data_bucket=bucket_name,
            database_name="analytics_db",
            target_table_name="cf_table",
            scripts_bucket="scripts-bucket",
            logical_name="analytics",
            iam_role_arn="arn:aws:iam::123456789012:role/GlueRole",
            git_repository="",
            git_owner="",
            git_branch="main",
            git_folder="glue-jobs",
            git_token="",
        )

        conf_value = mock_glue.create_job.call_args.kwargs["DefaultArguments"]["--conf"]
        expected_warehouse = f"spark.sql.catalog.glue_catalog.warehouse=s3://{bucket_name}/iceberg-warehouse/"
        assert expected_warehouse in conf_value, f"warehouse not using {bucket_name}"


class TestGitIntegration:
    """Preservation: Git 未設定時は False を返す (3.3)."""

    def test_all_present_returns_true(self):
        assert app.is_git_integration_enabled("repo", "owner", "token") is True

    def test_empty_repo_returns_false(self):
        assert app.is_git_integration_enabled("", "owner", "token") is False

    def test_empty_owner_returns_false(self):
        assert app.is_git_integration_enabled("repo", "", "token") is False

    def test_empty_token_returns_false(self):
        assert app.is_git_integration_enabled("repo", "owner", "") is False

    def test_whitespace_only_returns_false(self):
        assert app.is_git_integration_enabled("  ", "owner", "token") is False
