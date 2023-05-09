import os
import time

from dotenv import load_dotenv


load_dotenv(".env")

URL_PAGE = os.getenv('URL_PAGE')
EMAIL_USER = os.getenv('USER_EMAIL')
PASSWORD_USER = os.getenv('PASSWORD')
current_time = time.strftime("%Y%m%d-%H%M%S")


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(asctime)s -- %(message)s',
            'datefmt': '%y-%m-%d %H:%M:%S'
        },
        'detail': {
            'format': '%(asctime)s -- %(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s',
            'datefmt': '%y-%m-%d %H:%M:%S'
        },
        'informative': {
            'format': '%(asctime)s -- %(levelname)s -- %(message)s',
            'datefmt': '%y-%m-%d %H:%M:%S'
        }

    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'informative'
        },
        'file_simple': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'logs/test-log-{current_time}.log',
            'formatter': 'simple'
        },
        'file_informative': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'logs/test-log-{current_time}.log',
            'formatter': 'informative'
        }
    },
    'loggers': {
        'console': {
            'level': 'INFO',
            'handlers': ['console']
        },
        'file_simple': {
            'level': 'INFO',
            'handlers': ['file_simple']
        },
        'file_informative': {
            'level': 'INFO',
            'handlers': ['file_informative']
        }
    }
}

DEFAULT_LOGGER = 'file_simple'