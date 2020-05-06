import boto3
import os

client = boto3.client('pinpoint')

APP_ID = os.environ["APP_ID"]
SEG_ID = os.environ["SEG_ID"]

#Create a new segment on Pinpoint
def create_segment(feature, feature_value, channel, name):
    segment_version = client.get_segment(
                    ApplicationId=APP_ID,
                    SegmentId=SEG_ID
                    )['SegmentResponse']['Version']
    print(SEG_ID)
    return client.create_segment(
        ApplicationId=APP_ID,
        WriteSegmentRequest={
            'Name': name,
            'SegmentGroups': {
                'Groups': [
                    {
                        'Dimensions': [
                            {
                                'Attributes': {
                                    feature: {
                                        'AttributeType': 'INCLUSIVE',
                                        'Values': [
                                            feature_value
                                        ]
                                    }
                                },
                                'Demographic': {
                                    'Channel': {
                                        'DimensionType': 'INCLUSIVE',
                                        'Values': [
                                            channel,
                                        ]
                                    }
                                }
                            },
                        ],
                        'SourceSegments': [
                            {
                                'Id': SEG_ID,
                                'Version': segment_version
                            },
                        ],
                        'SourceType': 'ALL',
                        'Type': 'ANY'
                    },
                ],
                'Include': 'ANY'
            }
        }
    )
    

#Create a new campaign on Pinpoint
def create_campaign(seg_id, subject1, message1, subject2, message2):
    return client.create_campaign(
        ApplicationId=APP_ID,
        WriteCampaignRequest={
            'AdditionalTreatments': [
                {
                    'MessageConfiguration': {
                        'EmailMessage': {
                            'Body': message1,
                            'FromAddress': 'gw262@cornell.edu',
                            'Title': subject1
                        }
                    },
                    'SizePercent': 50,
                    'TreatmentDescription': 'test1',
                    'TreatmentName': 'test1',
                    'Schedule': {
                        'Frequency': 'ONCE',
                        'IsLocalTime': False,
                        'StartTime': 'IMMEDIATE',
                        'Timezone': 'UTC-05'
                    }
                }
            ],
            'MessageConfiguration': {
                'EmailMessage': {
                    'Body': message2,
                    'FromAddress': 'gw262@cornell.edu',
                    'Title': subject2
                }
            },
            'TreatmentDescription': 'test2',
            'TreatmentName': 'test2',
            'Schedule': {
                'Frequency': 'ONCE',
                'IsLocalTime': False,
                'StartTime': 'IMMEDIATE',
                'Timezone': 'UTC-05'
            },

            'Description': 'A/B test campaign for Chronicle',
            'Name': 'Chronicle Campaign',
            'SegmentId': seg_id,
            'SegmentVersion': 1
        }
    )

#Get the metadata associated with a given campaign
def get_campgin_info(campaign):
    campaign_info = client.get_campaign(ApplicationId=APP_ID, CampaignId=campaign)
    
    subject1 = campaign_info['CampaignResponse']['AdditionalTreatments'][0]['MessageConfiguration']['EmailMessage']['Title']
    message1 = campaign_info['CampaignResponse']['AdditionalTreatments'][0]['MessageConfiguration']['EmailMessage']['Body']
    treatment_id_1 = campaign_info['CampaignResponse']['AdditionalTreatments'][0]['Id']
    
    subject2 = campaign_info['CampaignResponse']['MessageConfiguration']['EmailMessage']['Title']
    message2 = campaign_info['CampaignResponse']['MessageConfiguration']['EmailMessage']['Body']
    treatment_id_2 = 0 if int(treatment_id_1) == 1 else 1
    
    return {
        str(treatment_id_1): {
            "subject": subject1,
            "body": message1
        },
        str(treatment_id_2): {
            "subject": subject2,
            "body": message2
        }
    }
    