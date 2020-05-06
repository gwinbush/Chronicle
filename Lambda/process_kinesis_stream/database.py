import boto3

table = boto3.resource('dynamodb').Table('chronicle-metrics')

def write_sent(event):
    campaign_id = event['attributes']['campaign_id']
    treatment_id = int(event['attributes']['treatment_id'])
    op_treatment_id = 0 if treatment_id == 1 else 1

    item = table.get_item(Key={'campaign_id': campaign_id})
    if 'Item' in item:
        #update table
        print("sent - updating entry")
        table.update_item(
            Key={
                'campaign_id': campaign_id
            },
            UpdateExpression="SET #met.#tid.#es = #met.#tid.#es + :inc",
            ExpressionAttributeNames={
                '#met': 'metrics',
                '#tid': str(treatment_id),
                '#es': 'emails_sent',
            },
            ExpressionAttributeValues={
                ':inc': 1
            },
        )
    else:
        #add new item to table
        print("sent - creating entry")
        response = table.put_item(
        Item={
            'campaign_id': campaign_id,
            'metrics': {
                str(treatment_id): {
                    'emails_sent': 1,
                    'emails_opened': 0
                },
                str(op_treatment_id): {
                    'emails_sent': 0,
                    'emails_opened': 0
                }
            }
        }
    )
    
    return 

def write_opened(event):
    campaign_id = event['attributes']['campaign_id']
    treatment_id = event['attributes']['treatment_id']
    op_treatment_id = 0 if treatment_id else 1
    
    item = table.get_item(Key={'campaign_id': campaign_id})
    if 'Item' in item:
        #update table
        print("open - updating entry")
        table.update_item(
            Key={
                'campaign_id': campaign_id
            },
            UpdateExpression="SET #met.#tid.#eo =  #met.#tid.#eo + :inc",
            ExpressionAttributeNames={
                '#met': 'metrics',
                '#tid': str(treatment_id),
                '#eo': 'emails_opened'
            },
            ExpressionAttributeValues={
                ':inc': 1
            },
        )
    else:
        #add new item to table
        print("open - creating entry")
        response = table.put_item(
        Item={
            'campaign_id': campaign_id,
            'metrics': {
                str(treatment_id): {
                    'emails_sent': 0,
                    'emails_opened': 1
                },
                str(op_treatment_id): {
                    'emails_sent': 0,
                    'emails_opened': 0
                }
            }
        }
    )
    
    return 