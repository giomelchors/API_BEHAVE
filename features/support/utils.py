import requests

from features.support.configuration import URL_PAGE, LOGGING_CONFIG, DEFAULT_LOGGER
import logging.config
from functools import wraps


def get_endpoint(endpoint, *args):
    if args:
        return URL_PAGE + endpoint.format(*args)
    return URL_PAGE + endpoint


instances = {}


def singleton(cls):
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


def request_exceptions(function):
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(DEFAULT_LOGGER)

    @wraps(function)
    def decorated(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            logger.exception(f"Http Error: {e}")
        except requests.exceptions.Timeout:
            logger.exception(f"Request took a long time to respond - Timeout Error")
        except requests.exceptions.RequestException as e:
            logger.exception(f"Could not send the request due to exception: {e}")

    return decorated
