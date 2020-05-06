import json
import boto3
import ast
import pinpoint
import dynamo
import base64


def lambda_handler(event, context):
    print(event)
    ROUTE = event['routeKey']
    
    
    if ROUTE == 'GET /api/v1/metrics':
        campaign_id = event['queryStringParameters']['campaign_id']
        metrics = dynamo.get_metrics(campaign_id)
        return metrics
            
    elif ROUTE == 'POST /api/v1/campaign':
        body = json.loads(base64.b64decode(event['body']))
        channel = body['distribution_channel']
        cohort_name = str(body['cohort_name'])
        cohort_value = str(body['cohort_value'])
        subject1 = str(body['subject1'])
        message1 = str(body['message1'])
        subject2 = str(body['subject2'])
        message2 = str(body['message2'])

        segment_resp = pinpoint.create_segment(cohort_name, cohort_value,\
                                            channel, 'testsegment')
        new_seg_id = segment_resp['SegmentResponse']['Id']
        campaign_resp = pinpoint.create_campaign(new_seg_id, subject1, message1,\
                                             subject2, message2)
        return campaign_resp
    
    elif ROUTE == 'GET /api/v1/campaigns/list':
        campaign_ids = dynamo.get_campaigns()
        return {
            "campaign_ids": campaign_ids
        }
    elif ROUTE == 'GET /api/v1/features':
        user_group = event['queryStringParameters']['user_group']
        features = dynamo.get_features(user_group)
        return features

    