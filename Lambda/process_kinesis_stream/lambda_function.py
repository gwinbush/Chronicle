import json
import base64
import boto3
import database

def lambda_handler(event, context):

    decoded_record_data = [base64.b64decode(record['kinesis']['data']) for record in event['Records']]
    deserialized_data = [json.loads(decoded_record) for decoded_record in decoded_record_data]
    print(deserialized_data)
    for data in deserialized_data:
        try:
            event_type = data['event_type']
            if event_type == '_campaign.send':
                database.write_sent(data)
            elif event_type == '_email.send':
                database.write_opened(data)
        except Exception as e:
            print(e)
            continue
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
