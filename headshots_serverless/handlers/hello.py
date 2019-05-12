import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    return "{} from Lambda!".format(os.environ['greeting'])
