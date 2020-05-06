import boto3
import pinpoint

table = boto3.resource('dynamodb').Table('chronicle-metrics')
user_info = boto3.resource('dynamodb').Table('user_info')



def get_metrics(campaign_id):
    #Get data from db
    item = table.get_item(Key={'campaign_id': campaign_id})
    item = item['Item']
    
    
    #Get data from pinpoint
    campaign_info = pinpoint.get_campgin_info(campaign_id)
    
    #Combine data
    return {
        'campaign_id': item['campaign_id'],
        '0': {
            'subject': campaign_info['0']['subject'],
            'body': campaign_info['0']['body'],
            'emails_sent': item['metrics']['0']['emails_sent'],
            'emails_opened': item['metrics']['0']['emails_opened']
        },
        '1': {
            'subject': campaign_info['1']['subject'],
            'body': campaign_info['1']['body'],
            'emails_sent': item['metrics']['1']['emails_sent'],
            'emails_opened': item['metrics']['1']['emails_opened']
        }
    }

#Get list of campaign ids from DynamoDB
def get_campaigns():
    return [item['campaign_id'] for item in table.scan()['Items']]

#Get list of features from DynamoDB    
def get_features(group):
    item = user_info.get_item(Key={'user_group': group})
    return item['Item']['features']