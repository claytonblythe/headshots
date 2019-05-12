import logging
from functools import wraps

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log_event(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        logger.debug(msg=kwargs['event'])
        return f(*args, **kwargs)

    return wrapper
