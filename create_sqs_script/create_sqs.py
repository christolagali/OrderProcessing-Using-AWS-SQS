import boto3



def checkQueueExists(OrderQueue):
    try:
        queue = sqs_client.get_queue_by_name(QueueName=OrderQueue)
        return queue
    except:
        return(False)

def createQueue(queuename):

	try:
		sqs_client = boto3.client('sqs',region_name='us-east-2')
	
		# creating a new queue
		
		if not checkQueueExists(queuename):
			queue = sqs_client.create_queue(QueueName=queuename, Attributes={'DelaySeconds': '5'})
		
			return(queue)
		
		else:
			return (queue)


	except Exception as e:
		print(e)



print(createQueue('OrderQueue'))