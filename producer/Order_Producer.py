import boto3
import pandas as pd
import time
import json
import sys,os,inspect
from pathlib import Path  
from os import path

sqs = boto3.client('sqs',region_name='us-east-2')
def getQueue(queuename):
	
	try:
		
		queue = sqs.get_queue_url(QueueName=queuename)
		
		return queue
	
	except Exception as e:
		raise e


try:
	# read data from file
	basepath = path.dirname(__file__)
	filepath = path.abspath(path.join(basepath, "..", "/data/","sales_data_sample.csv"))
	#print(filepath)
	#Path(filepath).name
	data = pd.read_csv('sales_data_sample.csv')
	
	dataDict = dict()
	
	queue = getQueue('OrderQueue')
	
	# emulate a producer by sending json data with a 3 second gap/delay

	"""
		For Demonstartion purposes we are sending the first 5 rows.
		Modify the range in the for loop to increase the no of rows to send.
	"""
	
	for i in range(0,5):
	
		# Build json object for SQS message Body
		dataDict['ordernumber'] = data.iloc[i]['ORDERNUMBER']
		dataDict['QUANTITYORDERED'] = data.iloc[i]['QUANTITYORDERED']
		dataDict['SALES'] = int(data.iloc[i]['SALES'])
		dataDict['STATUS'] = data.iloc[i]['STATUS']
		dataDict['CITY'] = data.iloc[i]['CITY']
		dataDict['COUNTRY'] = data.iloc[i]['COUNTRY']
    
		response = sqs.send_message(QueueUrl= queue['QueueUrl'], MessageBody=json.dumps(dataDict))

		# Using time module to add a delay of 3 seconds to emulate orders coming into SQS
		time.sleep(3)

		print(response)

except Exception as e:
	raise e

