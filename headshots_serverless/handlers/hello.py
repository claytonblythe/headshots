import os

from decorators import log_event


@log_event
def handler(event, context):
    return "{} from Lambda!".format(os.environ.get("greeting"))
