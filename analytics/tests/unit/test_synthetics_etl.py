"""
Unit tests for Synthetics ETL Lambda --conf and Git integration.

Validates:
- build_default_arguments includes all 4 glue_catalog settings (Bug #3 fix)
- is_git_integration_enabled returns True only when all 3 params non-empty (3.3)
- build_source_control_details detects provider correctly
- handle_create/handle_update pass full conf to Glue API

Requirements: 2.3, 2.4, 3.3
"""

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src" / "lambda-functions" / "synthetics-etl-handler"))

import app  # noqa: E402


GLUE_CATALOG_REQUIRED_SETTINGS = [
    "spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog",
    "spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog",
    "spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO",
    "spark.sql.catalog.glue_catalog.warehouse=s3://",
]


class TestBuildDefaultArguments:
    """Property: build_default_arguments MUST contain all 4 glue_catalog settings."""

    def test_conf_has_all_glue_catalog_settings(self):
        result = app.build_default_arguments("iceberg-bucket", "analytics_db", "table", "s3://source/")
        conf = result["--conf"]
        for setting in GLUE_CATALOG_REQUIRED_SETTINGS:
            assert setting in conf, f"--conf missing: {setting}"

    @pytest.mark.parametrize("bucket_name", [
        "my-iceberg-bucket",
        "analytics-iceberg-data-ap-northeast-1-857135586997",
        "bucket-with-special.chars-123",
    ])
    def test_warehouse_uses_iceberg_data_bucket(self, bucket_name):
        """Property: warehouse は常に s3://{iceberg_data_bucket}/iceberg-warehouse/ を使用."""
        result = app.build_default_arguments(bucket_name, "db", "table", "s3://src/")
        expected = f"spark.sql.catalog.glue_catalog.warehouse=s3://{bucket_name}/iceberg-warehouse/"
        assert expected in result["--conf"]

    def test_contains_extensions(self):
        result = app.build_default_arguments("bucket", "db", "table", "s3://src/")
        assert "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions" in result["--conf"]

    def test_contains_datalake_formats(self):
        result = app.build_default_arguments("bucket", "db", "table", "s3://src/")
        assert result["--datalake-formats"] == "iceberg"

    def test_contains_source_path(self):
        result = app.build_default_arguments("bucket", "db", "table", "s3://my-source/prefix/")
        assert result["--SOURCE_PATH"] == "s3://my-source/prefix/"


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

    def test_none_values_returns_false(self):
        assert app.is_git_integration_enabled(None, "owner", "token") is False


class TestBuildSourceControlDetails:
    """build_source_control_details が provider を正しく判定."""

    def test_github_provider(self):
        result = app.build_source_control_details("my-repo", "owner", "main", "folder", "token")
        assert result["Provider"] == "GITHUB"
        assert result["Owner"] == "owner"

    def test_gitlab_provider(self):
        result = app.build_source_control_details("gitlab-repo", "owner", "main", "folder", "token")
        assert result["Provider"] == "GITLAB"

    def test_codecommit_provider(self):
        result = app.build_source_control_details("codecommit-repo", "owner", "main", "folder", "token")
        assert result["Provider"] == "AWS_CODE_COMMIT"
        assert "Owner" not in result

    def test_bitbucket_provider(self):
        result = app.build_source_control_details("bitbucket-repo", "owner", "main", "folder", "token")
        assert result["Provider"] == "BITBUCKET"


class TestHandleCreateConf:
    """handle_create が Glue API に glue_catalog フル設定を渡す."""

    @patch.object(app, "glue_client")
    @patch.object(app, "wait_for_job_ready", return_value="arn:aws:glue:*:*:job/test")
    def test_create_passes_full_conf(self, mock_wait, mock_glue):
        mock_glue.create_job.return_value = {}

        app.handle_create(
            job_name="test-synthetics-job",
            script_location="s3://scripts/job.py",
            iceberg_data_bucket="iceberg-bucket",
            database_name="analytics_db",
            table_name="synthetics_canary_iceberg",
            source_path="s3://source/canary/",
            iam_role_arn="arn:aws:iam::123456789012:role/GlueRole",
            git_repository="", git_owner="", git_branch="main",
            git_folder="glue-jobs", git_token="",
        )

        conf = mock_glue.create_job.call_args.kwargs["DefaultArguments"]["--conf"]
        for setting in GLUE_CATALOG_REQUIRED_SETTINGS:
            assert setting in conf, f"handle_create --conf missing: {setting}"


class TestHandleUpdateConf:
    """handle_update が Glue API に glue_catalog フル設定を渡す."""

    @patch.object(app, "glue_client")
    @patch.object(app, "wait_for_job_ready", return_value="arn:aws:glue:*:*:job/test")
    def test_update_passes_full_conf(self, mock_wait, mock_glue):
        mock_glue.get_job.return_value = {
            "Job": {
                "Command": {"Name": "glueetl", "ScriptLocation": "s3://scripts/job.py", "PythonVersion": "3"},
                "DefaultArguments": {"--enable-metrics": "true"},
            }
        }
        mock_glue.update_job.return_value = {}

        app.handle_update(
            job_name="test-synthetics-job",
            script_location="s3://scripts/job.py",
            iceberg_data_bucket="iceberg-bucket",
            database_name="analytics_db",
            table_name="synthetics_canary_iceberg",
            source_path="s3://source/canary/",
            iam_role_arn="arn:aws:iam::123456789012:role/GlueRole",
            git_repository="", git_owner="", git_branch="main",
            git_folder="glue-jobs", git_token="",
        )

        conf = mock_glue.update_job.call_args.kwargs["JobUpdate"]["DefaultArguments"]["--conf"]
        for setting in GLUE_CATALOG_REQUIRED_SETTINGS:
            assert setting in conf, f"handle_update --conf missing: {setting}"
