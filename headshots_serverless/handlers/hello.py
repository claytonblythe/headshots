import os
import boto3

def handler(event, context):
    return "{} from Lambda!".format(os.environ['greeting'])
