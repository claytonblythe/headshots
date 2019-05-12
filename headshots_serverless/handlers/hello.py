import os

from decorators import log_event, log_environment, log_time


@log_event
@log_environment
@log_time
def handler(event, context):
    return "{} from Lambda!".format(os.environ.get("greeting"))
