# Changelog

## [Unreleased]

### Fixed

- **Bug #1 (GA4)**: Restore Iceberg table metadata (`table_type`, `metadata_location`) lost after Custom Resource update by adding `InputFormat`, `OutputFormat`, `SerdeInfo`, and `Version` to `GlueTableForGA4CoreReports` definition
- **Bug #2 (CloudFront)**: Persist `glue_catalog` Spark conf settings across Custom Resource updates by including full `--conf` in `handle_update`
- **Bug #3 (Synthetics)**: Persist `glue_catalog` Spark conf settings for Synthetics job (same root cause as Bug #2)
- **Bug #4 (Synthetics)**: Enable Git source control integration for Synthetics Visual ETL job via Custom Resource
- **Bug #5 (GA4)**: Sync `CodeGenConfigurationNodes` on Custom Resource update to ensure `SchemaChangePolicy` (EnableUpdateCatalog) is applied

### Added

- `SecretString` property to `SecretsManagerSecretForGA4` — populates OAuth tokens from parameters on initial creation, preventing Connection creation failure
- Unit tests for GA4 Visual ETL node generation (`tests/unit/test_ga4_visual_etl.py`)
- Unit tests for CloudFront ETL conf generation (`tests/unit/test_cloudfront_etl_conf.py`)

### Changed

- Custom Resource `handle_update` now sends full job configuration (including `CodeGenConfigurationNodes` and `--conf`) instead of infrastructure-only updates
- Synthetics job management migrated from native `AWS::Glue::Job` to Lambda-backed Custom Resource (enables Git integration and consistent `--conf` handling)
