import logging
from functools import wraps
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log_event(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        logger.info("#EVENT")
        logger.info(msg=args[0])
        return f(*args, **kwargs)

    return wrapper


def log_environment(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        logger.info("#ENVIRONMENT")
        logger.info(msg=os.environ)
        return f(*args, **kwargs)

    return wrapper
