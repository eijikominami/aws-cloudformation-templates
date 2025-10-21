# AWS CloudFormation Templates Project Structure

## Project Overview

This repository provides a comprehensive collection of production-ready AWS CloudFormation templates organized by service categories. The templates implement AWS best practices for security, monitoring, and architecture patterns.

### Key Features
- **Production-Ready**: Templates include proper security configurations, monitoring, and alerting
- **Modular Design**: Can be used independently or combined for complex architectures  
- **Comprehensive Coverage**: Security, networking, monitoring, analytics, media, CI/CD, and more
- **Multi-Language Support**: Documentation in English and Japanese
- **SAM Integration**: Serverless Application Model for Lambda-based solutions

### Primary Use Cases
- Secure AWS environment setup with centralized logging and monitoring
- Standardized security configurations across AWS accounts
- Analytics pipelines and data processing workflows
- Web application deployment with CI/CD pipelines
- Multi-account governance and compliance

### Architecture Patterns
- Multi-account security with AWS Organizations
- Centralized logging (S3 + OpenSearch)
- Static website hosting with CloudFront
- Container applications with ECS
- Analytics pipelines with AWS Glue

## Top-Level Organization
```
aws-cloudformation-templates/
├── {service-category}/          # Service-specific templates
│   ├── README.md               # Category documentation (EN)
│   ├── README_JP.md           # Category documentation (JP)  
│   ├── templates/             # CloudFormation templates
│   ├── sam-app/              # SAM applications (if applicable)
│   └── readme/               # Additional documentation
├── images/                   # Architecture diagrams and screenshots
└── shared/                  # Reusable components and utilities
```

## Service Categories
- **aiml/**: AI/ML services (Bedrock, Kendra)
- **analytics/**: Data analytics (Glue, analytics pipelines)
- **cicd/**: CI/CD pipelines (CodeBuild, CodePipeline)
- **cloudops/**: Operations (Systems Manager, monitoring)
- **edge/**: Edge services (CloudFront, WAF)
- **identity/**: Identity management (IAM, Identity Center)
- **media/**: Media services (MediaLive, MediaConnect)
- **monitoring/**: CloudWatch alarms and dashboards
- **network/**: Networking (VPC, Transit Gateway, Route53)
- **notification/**: Messaging (SNS, EventBridge, Chatbot)
- **security/**: Security services (GuardDuty, Security Hub, Config)
- **storage/**: Storage services (FSx)
- **web-servers/**: Web application hosting (ECS, Auto Scaling)

## File Naming Conventions
- **Templates**: `{service-name}.yaml` or `template.yaml` for main template
- **Documentation**: `README.md` (English), `README_JP.md` (Japanese)
- **SAM Apps**: Organized in `sam-app/` with `template.yaml`
- **Lambda Code**: Separate directories per function in `sam-app/`

## Template Structure Standards
- Use YAML format for all CloudFormation templates
- Include comprehensive parameter descriptions
- Provide meaningful output values
- Follow AWS resource naming conventions
- Include proper tags and metadata