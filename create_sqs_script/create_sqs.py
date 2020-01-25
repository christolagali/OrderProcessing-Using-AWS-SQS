import boto3


try:
	sqs_client = boto3.client('sqs',region_name='us-east-2')
	
	# creating a new queue
	queue = sqs_client.create_queue(QueueName='OrderQueue', Attributes={'DelaySeconds': '5'})
	
	return(queue)
	


except Exception as e:
	print(e)
