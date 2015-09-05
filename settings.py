__author__ = 'twisted'

NODE = 'node'
CONFIG_PATH = './settings.ini'


class AppiumOptions:
    DEFAULT_OPTIONS = '--log-no-colors '
    TIME_STAMP= '--log-timestamp '
    LOG_LEVEL_TEMPLATE = '--log-level={} '


class LogLevel:
    DEBUG = 'debug'
    INFO = 'info'
    WARN = 'warn'
    ERROR = 'error'
