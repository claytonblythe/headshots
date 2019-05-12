from .lambda_decorators import before
import logging


@before
def log_event(event, context):
    logging.debug(event)
    return event, context
