# README Format Guidelines

This document defines the comprehensive standard format for README files in the aws-cloudformation-templates project. It serves as a complete reference for maintaining consistency across all service documentation.

## Project Overview

This project contains CloudFormation templates for various AWS services, organized in alphabetical folders. Each service folder contains:
- `README.md` (English documentation)
- `README_JP.md` (Japanese documentation)  
- `templates/` folder with CloudFormation YAML files

## Standard Format Structure

### Mandatory Section Order and Naming
All README files MUST follow this exact structure and naming:

1. **Header Section** (MANDATORY)
   - Language navigation links: `English / [**日本語**](README_JP.md)`
   - Service title with project path: `# AWSCloudFormationTemplates/[service-name]`
   - Build status badges and GitHub metadata (3 badges required)
   - Brief service description (1-2 sentences)

2. **Prerequisites Section** (MANDATORY)
   - Section title: `## Prerequisites`
   - Service-specific deployment requirements only
   - Format: `Before deploying this template, ensure you have:`
   - Bullet points with specific requirements
   - Excludes general AWS requirements (CLI, basic IAM, etc.)

3. **TL;DR Section** (MANDATORY)
   - Section title: `## TL;DR` (NEVER use service name as section title)
   - Quick deployment buttons for AWS Console
   - Organized in table format with regions
   - Individual service deployment options if applicable

4. **Architecture Section** (RECOMMENDED)
   - Section title: `## Architecture`
   - Architecture diagrams when available
   - Component descriptions
   - May be omitted if no architecture diagram exists

5. **Deployment Section** (RECOMMENDED)
   - Section title: `## Deployment`
   - CLI command examples
   - Parameter tables with detailed descriptions
   - May be omitted for simple services

6. **Service-Specific Sections** (OPTIONAL)
   - Detailed configuration instructions
   - Service-specific notes and warnings
   - Use descriptive section names

7. **Troubleshooting Section** (MANDATORY)
   - Section title: `## Troubleshooting`
   - Service-specific problem resolution
   - Organized by problem category
   - Must be the last section

### Template URL Structure
**Critical**: Template URLs differ between README buttons and CLI commands:
- **README Deploy Buttons**: Use S3 URLs WITHOUT `/templates/` path
  - Example: `https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/edge/cloudfront.yaml`
- **CLI Commands**: Use local paths WITH `templates/` folder
  - Example: `aws cloudformation deploy --template-file templates/cloudfront.yaml`

This difference exists because the CI/CD process (buildspec-upload-artifacts-s3.yml) uploads files from `[service]/templates/` to S3 at `aws-cloudformation-templates/[service]/` (flattening the structure).

## New Standard Format Additions

### Prerequisites Section
- **Purpose**: List deployment requirements specific to the service
- **Placement**: After service description, before TL;DR section
- **Content Rules**:
  - ✅ Include: Service-specific requirements (certificates, domain names, existing resources)
  - ❌ Exclude: General requirements (AWS CLI, basic IAM permissions, general AWS knowledge)
- **English Format**: 
  ```markdown
  ## Prerequisites
  
  Before deploying this template, ensure you have:
  
  - Service-specific requirement 1
  - Service-specific requirement 2
  ```
- **Japanese Format**:
  ```markdown
  ## 前提条件
  
  デプロイの前に以下を準備してください。
  
  - サービス固有の要件 1
  - サービス固有の要件 2
  ```

### Troubleshooting Section
- **Purpose**: Provide solutions for common service-specific issues
- **Placement**: At the end of the document
- **Content Rules**:
  - ✅ Include: Service-specific problems and solutions
  - ❌ Exclude: General AWS troubleshooting, basic CloudFormation issues
- **Structure**: Organize by service component or issue type
- **English Format**:
  ```markdown
  ## Troubleshooting
  
  ### Service-Specific Issue Category
  
  If you encounter [specific problem]:
  
  1. Step 1 to resolve
  2. Step 2 to resolve
  3. Step 3 to resolve
  ```
- **Japanese Format**:
  ```markdown
  ## トラブルシューティング
  
  ### サービス固有の問題カテゴリ
  
  [具体的な問題] が発生した場合：
  
  1. 解決手順 1
  2. 解決手順 2
  3. 解決手順 3
  ```

## Japanese README Specific Guidelines

### 1. Spacing Rules (Critical for Readability)
- **Rule**: Always add spaces between Japanese text and English words/acronyms
- **Examples**: 
  - ❌ `アプリケーション用に設定されたOAuth 2.0認証情報`
  - ✅ `アプリケーション用に設定された OAuth 2.0 認証情報`
  - ❌ `CloudFrontディストリビューション`
  - ✅ `CloudFront ディストリビューション`
  - ❌ `VPCとサブネット`
  - ✅ `VPC とサブネット`

### 2. Terminology Consistency
- **Service Names**: Keep AWS service names in English with proper spacing
  - ✅ `Amazon S3 バケット`
  - ✅ `AWS Lambda 関数`
  - ✅ `Amazon CloudWatch アラーム`
- **Technical Terms**: Use consistent Japanese translations
  - `deployment` → `デプロイ`
  - `template` → `テンプレート`
  - `parameter` → `パラメータ`
  - `troubleshooting` → `トラブルシューティング`

### 3. Sentence Structure
- **Prerequisites**: Always start with `デプロイの前に以下を準備してください。`
- **Troubleshooting**: Use `[問題] が発生した場合：` format
- **Descriptions**: Maintain formal but accessible tone

## Implementation Guidelines

### Work Approach
- **Method**: Complete one service entirely before moving to the next
- **Order**: Alphabetical order by folder name
- **Scope**: Both README.md (English) and README_JP.md (Japanese)

### Section Implementation Rules
- **Prerequisites**: Always mandatory, must be service-specific only
- **TL;DR**: Always mandatory, never use service name as title
- **Architecture**: Include if architecture diagram exists
- **Deployment**: Include if complex deployment steps exist
- **Troubleshooting**: Always mandatory, must be last section

### YAML Consistency Check
- **When YAML exists**: Check for discrepancies and update outdated information
- **When YAML doesn't exist**: List the service in chat for review
- **SAM applications**: List both template.yaml and SAM app contents, merge common parts

### Information Accuracy
- **Service-specific requirements**: Must be verified using AWS MCP or official documentation
- **No speculation**: Do not guess or assume service requirements
- **Verification required**: All technical details must be confirmed before inclusion

### Special Cases Handling
- **Services with no templates**: Create README with basic structure and note template absence
- **Services with multiple sub-services**: Use individual deployment tables in TL;DR
- **Services with complex architecture**: Include detailed Architecture section
- **Services with simple deployment**: May omit Deployment section if TL;DR is sufficient

## Conditional Application

The new standard format should be applied when:
- ✅ Information is available and accurate
- ✅ It adds value for users
- ✅ It doesn't create confusion

The new standard format should NOT be applied when:
- ❌ Information is insufficient
- ❌ It would cause confusion
- ❌ A simpler format is more appropriate

## File Structure and Naming Conventions

### Directory Structure
```
aws-cloudformation-templates/
├── [service-name]/
│   ├── README.md (English)
│   ├── README_JP.md (Japanese)
│   └── templates/
│       ├── template.yaml (main template)
│       └── [other-templates].yaml
└── README_FORMAT_GUIDELINES.md (this file)
```

### File Naming Rules
- **README Files**: Always `README.md` and `README_JP.md`
- **Template Files**: Use descriptive names matching service functionality
- **Language Links**: Use relative paths: `[**日本語**](README_JP.md)` and `[**English**](README.md)`

## Quality Assurance

### Mandatory Format Compliance Checklist
- [ ] **Header Section**
  - [ ] Language navigation links present and correct
  - [ ] Service title follows exact format: `# AWSCloudFormationTemplates/[service-name]`
  - [ ] All 3 badges present (Build Status, License, Release)
  - [ ] Brief service description (1-2 sentences)
- [ ] **Section Naming**
  - [ ] Prerequisites section titled exactly `## Prerequisites`
  - [ ] TL;DR section titled exactly `## TL;DR` (NEVER service name)
  - [ ] Architecture section titled exactly `## Architecture` (if present)
  - [ ] Deployment section titled exactly `## Deployment` (if present)
  - [ ] Troubleshooting section titled exactly `## Troubleshooting`
- [ ] **Section Order**
  - [ ] Prerequisites comes immediately after service description
  - [ ] TL;DR comes after Prerequisites
  - [ ] Troubleshooting is the last section
  - [ ] All sections follow mandatory order

### Content Quality Checklist
- [ ] **Prerequisites Section**
  - [ ] Contains only service-specific requirements
  - [ ] Excludes general AWS/CLI requirements
  - [ ] Uses correct format for both languages
  - [ ] Starts with "Before deploying this template, ensure you have:"
- [ ] **Template URLs**
  - [ ] Deploy buttons use S3 URLs WITHOUT `/templates/`
  - [ ] CLI commands use local paths WITH `templates/`
- [ ] **Troubleshooting Section**
  - [ ] Addresses service-specific issues only
  - [ ] Provides actionable solutions
  - [ ] Organized by logical categories
  - [ ] Is the final section in the document
- [ ] **Japanese Formatting**
  - [ ] Spaces between Japanese text and English words
  - [ ] Consistent terminology usage
  - [ ] Proper sentence structure
- [ ] **Technical Accuracy**
  - [ ] YAML consistency verified
  - [ ] All information verified via AWS documentation or MCP
  - [ ] No speculation or assumptions

### Final Review Checklist
- [ ] **File Updates**
  - [ ] English README.md updated
  - [ ] Japanese README_JP.md updated
  - [ ] Both files follow respective guidelines
- [ ] **Content Quality**
  - [ ] No speculation or unverified information
  - [ ] Service-specific focus maintained
  - [ ] Format matches new standard structure exactly
- [ ] **Cross-References**
  - [ ] Language navigation links work correctly
  - [ ] All referenced files exist
  - [ ] Template URLs are accessible

### Common Violations to Avoid
- [ ] **NEVER** use service name as TL;DR section title (e.g., "## Security", "## Network")
- [ ] **NEVER** omit Prerequisites or Troubleshooting sections
- [ ] **NEVER** place Troubleshooting section before the end
- [ ] **NEVER** include general AWS requirements in Prerequisites
- [ ] **NEVER** use inconsistent section naming

## Common Issues and Solutions

### Template URL Problems
- **Issue**: Deploy buttons return 404 errors
- **Solution**: Verify S3 URL structure excludes `/templates/` path

### Japanese Spacing Issues
- **Issue**: Text appears cramped or hard to read
- **Solution**: Add spaces between Japanese and English text systematically

### Prerequisites Scope Creep
- **Issue**: Prerequisites become too general
- **Solution**: Focus only on service-specific requirements, exclude AWS basics

### Troubleshooting Overlap
- **Issue**: Troubleshooting becomes too generic
- **Solution**: Address only service-specific problems with concrete steps

## Section-Specific Guidelines

### Header Section Requirements
```markdown
English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/[service-name]
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=...)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/[service-name]`` [brief description].
```

### Prerequisites Section Template (MANDATORY FORMAT)
```markdown
## Prerequisites

Before deploying this template, ensure you have:

- [Service-specific requirement 1]
- [Service-specific requirement 2]
- [Service-specific requirement 3]
```

**CRITICAL RULES:**
- MUST start with exactly: `Before deploying this template, ensure you have:`
- NEVER start directly with bullet points
- For monitoring services: Use `Before deploying these monitoring templates, ensure you have:`
- Japanese version MUST use: `デプロイの前に以下を準備してください。`

### TL;DR Section Template (MANDATORY FORMAT)

**For services with single main template:**
```markdown
## TL;DR

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](URL) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](URL) |

If you want to deploy each service individually, click the button below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| [Service Name] | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](URL) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](URL) |
```

**For services with only individual services (no main template):**
```markdown
## TL;DR

If you want to deploy each service individually, click the button below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| [Service Name] | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](URL) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](URL) |
```

**CRITICAL RULES:**
- MUST use exactly: `If you just want to deploy the stack, click the button below.`
- MUST use exactly: `If you want to deploy each service individually, click the button below.`
- NEVER use variations like "click the buttons below" or "click one of the two buttons below"
- NEVER use "follow these steps" instead of "click the button below"
- Japanese version MUST use: `以下のボタンをクリックすることで、CloudFormation をデプロイすることが可能です。`

### Troubleshooting Section Template
```markdown
## Troubleshooting

### [Problem Category 1]

If [specific problem description]:

1. [Step 1 to resolve]
2. [Step 2 to resolve]
3. [Step 3 to resolve]

### [Problem Category 2]

If [specific problem description]:

1. [Step 1 to resolve]
2. [Step 2 to resolve]
```

## Maintenance Notes

- **Update Frequency**: Guidelines should be updated when new patterns emerge
- **Version Control**: Track changes to maintain consistency across updates
- **Feedback Integration**: Incorporate lessons learned from each service update
- **Documentation Sync**: Keep this guide aligned with actual implementation practices
- **Format Enforcement**: All new README files must pass the quality assurance checklist