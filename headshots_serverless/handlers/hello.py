import os

from decorators import log_event, log_environment


@log_event
@log_environment
def handler(event, context):
    return "{} from Lambda!".format(os.environ.get("greeting"))
