# Project Overview  
Link to website: http://chronicle-webapp.s3-website-us-east-1.amazonaws.com

## Requirements  
----
A/B Testing Platform  
 
Send two messages to two groups of customers. See how many customers open each message.  

#### Features:  
- Choose two groups based of customer metadata  
- Send message (email, sms, app notification) to each group  
- Collect metrics from each group  
- (Potential feature) Add new customers with metadata  

## Design  
----
#### Front-end  
- Allow users to perform each action described in features section
- Vue single page app hosted on S3

#### Back-end 
- Lambda + API Gateway to handle user input and make appropriate API calls to AWS Pinpoint
- User data (user id, campaign ids) stored in DynamoDB
- Customer data (customer id, metadata) stored in DynamoDB and used to update segments on AWS Pinpoint when user submits new campaign with selected cohort

## API
----

#### URL  
  `/api/v1/metrics`
#### Method  
  `GET`
#### URL Params
   *Required:* `campaign_id=[string]`
#### Sample Call
    curl --location --request GET 'https://drtk2lbaij.execute-api.us-east-1.amazonaws.com/api/v1/metrics?campaign_id=223090a049644f8a8c82b09c33be6594'


#### URL  
  `/api/v1/campaigns/list`
#### Method  
  `GET`
#### Sample Call
    curl --location --request GET 'https://drtk2lbaij.execute-api.us-east-1.amazonaws.com/api/v1/campaigns/list'

#### URL  
  `/api/v1/features`
#### Method  
  `GET`
#### URL Params
   *Required:* `user_group=[string]`
#### Sample Call
    curl --location --request GET https://drtk2lbaij.execute-api.us-east-1.amazonaws.com/api/v1/features?user_group=group_0

#### URL  
  `/api/v1/features`
#### Method  
  `GET`
#### Data Params
   *Required:*  
    
    {  
        "distribution_channel": [string],
        "cohort_name": [string],
        "cohort_value": [string],
        "subject1": [string],
        "message1": [string],  
        "subject2": [string],  
        "message2": [string]  
    }  
#### Sample Call
    curl --location --request POST 'https://drtk2lbaij.execute-api.us-east-1.amazonaws.com/api/v1/campaign' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "distribution_channel": "EMAIL",
            "cohort_name": "age",
            "cohort_value": "21",
            "subject1": "Hello valued customer",
            "message1": "Please buy our product",
            "subject2": "Warning!",
            "message2": "New study shows that 100% of people without our product are unhappy"
        }'
        




## Architecture diagram  
----
![architecture](architecture.png)