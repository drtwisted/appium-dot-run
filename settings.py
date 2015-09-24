__author__ = 'twisted'
from os.path import abspath, dirname

NODE = 'node'
BASE_PATH = abspath(dirname(__file__))
CONFIG_PATH = '{}/settings.ini'.format(BASE_PATH)


class AppiumOptions:
    DEFAULT_OPTIONS = '--log-no-colors '
    TIME_STAMP= '--log-timestamp '
    LOG_LEVEL_TEMPLATE = '--log-level={} '


class LogLevel:
    DEBUG = 'debug'
    INFO = 'info'
    WARN = 'warn'
    ERROR = 'error'
