import os
import logging.config

HOST = '0.0.0.0'
PORT = 5555

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_FILES_DIR = os.path.join(PROJECT_DIR, 'static_files')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(module)s %(process)d %(thread)d %(levelname)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file-log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'run.log',
            'when': 'midnight',
        },
    },
    'loggers': {
        'simpleHttpServer': {
            'handlers':['file-log', 'console'],
            'propagate': False,
            'level':'DEBUG',
        },
    },
}


def setup_logging():
    logging.config.dictConfig(LOGGING)

