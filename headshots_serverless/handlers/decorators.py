import logging
from functools import wraps

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log_event(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        logger.info(msg=args)
        logger.info(msg=kwargs)
        return f(*args, **kwargs)

    return wrapper
