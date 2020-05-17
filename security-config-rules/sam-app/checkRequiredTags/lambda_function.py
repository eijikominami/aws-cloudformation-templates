import logging
import json
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

# Specify desired resource types to validate
APPLICABLE_RESOURCES = ["AWS::ApiGateway::RestApi", "AWS::Lambda::Function"]

logger = logging.getLogger()
logger.setLevel(20)

# Iterate through required tags ensureing each required tag is present, 
# and value is one of the given valid values
@xray_recorder.capture('find_violation')
def find_violation(current_tags, required_tags):
    tagkey = ""
    tagValue = ""

    for rtag,rvalues in required_tags.items():
        if rtag == 'tagKey':
            tagkey = rvalues
        if rtag == 'tagValue':
            tagValue = rvalues

    if len(tagkey)>0 and len(tagValue)>0:
        for ctag,cvalues in current_tags.items():
            if ctag == tagkey and cvalues == rvalues:
                return None
        return "Required tags dose NOT match any of existing tags."
    else:
        return "Required tags dose NOT be defined."

@xray_recorder.capture('evaluate_compliance')
def evaluate_compliance(configuration_item, rule_parameters):
    
    if configuration_item["resourceType"] not in APPLICABLE_RESOURCES:
        return {
            "compliance_type": "NOT_APPLICABLE",
            "annotation": "The rule doesn't apply to resources of type " +
            configuration_item["resourceType"] + "."
        }

    if configuration_item["configurationItemStatus"] == "ResourceDeleted":
        return {
            "compliance_type": "NOT_APPLICABLE",
            "annotation": "The configurationItem was deleted and therefore cannot be validated."
        }
    
    # API Gateway
    if configuration_item["resourceType"] == "AWS::ApiGateway::RestApi":
        client = boto3.client('apigateway')
        
        all_tags = client.get_rest_api(restApiId=configuration_item["ARN"][-10:])
        current_tags = all_tags['tags']

    # Lambda
    if configuration_item["resourceType"] == "AWS::Lambda::Function":
        client = boto3.client('lambda')
        
        all_tags = client.list_tags(Resource=configuration_item["ARN"])
        current_tags = all_tags['Tags']  # get only user tags.  

    violation = find_violation(current_tags, rule_parameters)        

    if violation:
        return {
            "compliance_type": "NON_COMPLIANT",
            "annotation": violation
        }

    return {
        "compliance_type": "COMPLIANT",
        "annotation": "This resource is compliant with the rule."
    }

@xray_recorder.capture('lambda_handler')
def lambda_handler(event, context):
    invoking_event = json.loads(event["invokingEvent"])
    logger.info(event)

    configuration_item = invoking_event["configurationItem"]
    
    rule_parameters = json.loads(event["ruleParameters"])
    
    result_token = "No token found."
    if "resultToken" in event:
        result_token = event["resultToken"]

    evaluation = evaluate_compliance(configuration_item, rule_parameters)

    config = boto3.client("config")
    config.put_evaluations(
        Evaluations=[
            {
                "ComplianceResourceType":
                    configuration_item["resourceType"],
                "ComplianceResourceId":
                    configuration_item["resourceId"],
                "ComplianceType":
                    evaluation["compliance_type"],
                "Annotation":
                    evaluation["annotation"],
                "OrderingTimestamp":
                    configuration_item["configurationItemCaptureTime"]
            },
        ],
        ResultToken=result_token
    )