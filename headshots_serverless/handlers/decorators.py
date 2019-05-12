import logging
from functools import wraps
import os
from datetime import datetime

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
        logger.info(msg=os.environ.__dict__._data)
        return f(*args, **kwargs)
    return wrapper


def log_time(f):
    @wraps(f)
    def wrapper(*args, **kw):
        # Before function call
        before_time = datetime.utcnow()
        output = f(*args, **kw)
        logger.info(f"Function {f.__name__} execution time: {(datetime.utcnow()-before_time).total_seconds()} s")
        return output
    return wrapper
