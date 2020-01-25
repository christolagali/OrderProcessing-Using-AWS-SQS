import boto3
import pandas as pd
import time
import json


def getQueue():
	
	try:
		sqs = boto3.client('sqs',region_name='us-east-2')
		queue = sqs.get_queue_url(QueueName='OrderQueue')
		
		return queue
	
	except Exception as e:
		raise e


try:
	# read data from file
	data = pd.read_csv('/home/ec2-user/sales_data_sample.csv')
	
	dataDict = dict()
	
	queue = getQueue()
	
	# emulate a producer by sending json data with a 3 second gap/delay
	
	for i in range(0,5):
	
		# Build json object for SQS message Body
		dataDict['ordernumber'] = data.iloc[i]['ORDERNUMBER']
		dataDict['QUANTITYORDERED'] = data.iloc[i]['QUANTITYORDERED']
		dataDict['SALES'] = int(data.iloc[i]['SALES'])
		dataDict['STATUS'] = data.iloc[i]['STATUS']
		dataDict['CITY'] = data.iloc[i]['CITY']
		dataDict['COUNTRY'] = data.iloc[i]['COUNTRY']
    
		response = sqs.send_message(QueueUrl= queue['QueueUrl'], MessageBody=json.dumps(dataDict))
    
		time.sleep(3)
    
		print(response)
	
	
	
	
	
	

except Exception as e:
	raise e

