import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    client = boto3.client('s3')
    client.put_object(Bucket="claytondblythe-headshots-dev", Key="test", Body=os.environ['greeting'])
    return "{} from Lambda!".format(os.environ['greeting'])
