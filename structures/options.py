__author__ = 'twisted'


class AppiumOptions:
    DEFAULT_OPTIONS = '--log-no-colors '
    TIME_STAMP= '--log-timestamp '
    LOG_LEVEL_TEMPLATE = '--log-level={} '


class LogLevel:
    DEBUG = 'debug'
    INFO = 'info'
    WARN = 'warn'
    ERROR = 'error'