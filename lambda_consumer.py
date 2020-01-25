import json
import boto3
import string
import json

s3 = boto3.resource("s3")
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
dynamoTable = dynamodb.Table('OrderDetails')

def lambda_handler(event, context):
    # TODO implement

    try:
		
		# Iterate through each SQS message
        for rec in event['Records']:
            #print('I got Triggered!')
			
			# Process each SQS message and insert into the Orders Table in dynamodb
            dynamoTable.put_item(Item=json.loads(rec['body']) )
            
            
            
        
    
    except Exception as e:
        
        print(e)
        raise e
        
