__author__ = 'twisted'
from configparser import ConfigParser


class ConfigHandler(ConfigParser):
    def __init__(self, config_path):
        ConfigParser.__init__(self)
        self.__path = config_path
        self.read()

    def read(self):
        ConfigParser.read(self, self.__path)

    def save(self):
        if self.__path:
            with open(self.__path, 'w') as _file:
                ConfigParser.write(self, _file)


class AppiumRunnerConfig(ConfigHandler):
    def __init__(self, config_path):
        ConfigHandler.__init__(self, config_path=config_path)
        self.__identity = 'appiumrunner'
        self.opt_appiumlocation = 'appium_location'
        self.opt_loglevel = 'log_level'
        self.opt_timestamp = 'time_stamp'
        self.opt_coloroutput = 'color_output'

    def __bool_getter(self, param):
        val = str(self.get(self.__identity, param))
        if val.lower() == 'yes':
            return True
        elif val.lower() == 'no':
            return False

    def __bool_setter(self, param, value):
        if value:
            val = 'yes'
        else:
            val = 'no'

        self.set(self.__identity, param, val)

    @property
    def is_valid(self):
        return self.__identity in self.sections()

    @property
    def appium_location(self):
        return str(self.get(self.__identity, self.opt_appiumlocation))

    @appium_location.setter
    def appium_location(self, path):
        self.set(self.__identity, self.opt_appiumlocation, path)

    @property
    def log_level(self):
        return str(self.get(self.__identity, self.opt_loglevel)).lower()

    @log_level.setter
    def log_level(self, level):
        self.set(self.__identity, self.opt_loglevel, level)

    @property
    def time_stamp(self):
        return self.__bool_getter(self.opt_timestamp)

    @time_stamp.setter
    def time_stamp(self, show):
        self.__bool_setter(self.opt_timestamp, show)

    @property
    def color_output(self):
        return self.__bool_getter(self.opt_coloroutput)

    @color_output.setter
    def color_output(self, use):
        self.__bool_setter(self.opt_coloroutput, use)
