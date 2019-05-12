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
        os_env = os.environ
        env_dict = {os_env.decodekey(key): os_env.decodevalue(value) for key, value in os_env._data.items()}
        logger.info(msg=env_dict)
        return f(*args, **kwargs)
    return wrapper


def log_duration(f):
    @wraps(f)
    def wrapper(*args, **kw):
        # Before function call
        begin_time = datetime.utcnow()
        output = f(*args, **kw)
        elapsed_time = (datetime.utcnow()-begin_time).total_seconds()
        logger.info(f"Function {f.__name__} execution time: {elapsed_time} s")
        return output
    return wrapper
