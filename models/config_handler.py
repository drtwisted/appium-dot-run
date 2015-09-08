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
        
        # Log options
        self.opt_loglevel = 'log_level'
        self.opt_timestamp = 'time_stamp'
        self.opt_coloroutput = 'color_output'
        self.opt_uselocaltimezon = 'use_local_timezone'
        self.opt_writetolog = 'write_to_log'
        self.opt_logfilepath = 'log_path'
        
        # Server options
        self.opt_showstartupcommand = 'show_startup_command'
        self.opt_serveraddress = 'server_address'
        self.opt_serverport = 'server_port'
        self.opt_commandtimeout = 'command_timeout'
        
        # Test application options
        self.opt_apppath = 'app_path'
        self.opt_appnoreset = 'app_no_reset'
        self.opt_apppackage = 'app_package'
        self.opt_appactivity = 'app_activity'
        self.opt_appwaitactivity = 'app_wait_activity'
        
        # Device options
        self.opt_devicereadytimeout = 'device_ready_timeout'
        self.opt_devicename = 'device_name'

    def __bool_getter(self, param):
        val = str(self.get(self.__identity, param)).lower()
        if val == 'yes':
            return True
        elif val == 'no':
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

    @property
    def use_local_timezone(self):
        return self.__bool_getter(self.opt_coloroutput)

    @use_local_timezone.setter
    def use_local_timezone(self, use):
        self.__bool_setter(self.opt_coloroutput, use)

    @property
    def write_to_log(self):
        return self.__bool_getter(self.opt_coloroutput)

    @write_to_log.setter
    def write_to_log(self, use):
        self.__bool_setter(self.opt_coloroutput, use)

    @property
    def logfile_path(self):
        return self.__bool_getter(self.opt_coloroutput)

    @logfile_path.setter
    def logfile_path(self, use):
        self.__bool_setter(self.opt_coloroutput, use)

    @property
    def show_startup_command(self):
        return self.__bool_getter(self.opt_coloroutput)

    # Server options
    @show_startup_command.setter
    def show_startup_command(self, use):
        self.__bool_setter(self.opt_coloroutput, use)

    @property
    def server_address(self):
        return self.__bool_getter(self.opt_coloroutput)

    @server_address.setter
    def server_address(self, use):
        self.__bool_setter(self.opt_coloroutput, use)

    @property
    def server_port(self):
        return self.__bool_getter(self.opt_coloroutput)

    @server_port.setter
    def server_port(self, use):
        self.__bool_setter(self.opt_coloroutput, use)
        
    @property
    def command_timeout(self):
        return self.__bool_getter(self.opt_coloroutput)

    @command_timeout.setter
    def command_timeout(self, use):
        self.__bool_setter(self.opt_coloroutput, use)

    # Test application options
    @property
    def app_path(self):
        return self.__bool_getter(self.opt_coloroutput)

    @app_path.setter
    def app_path(self, use):
        self.__bool_setter(self.opt_coloroutput, use)

    @property
    def app_no_reset(self):
        return self.__bool_getter(self.opt_coloroutput)

    @app_no_reset.setter
    def app_no_reset(self, use):
        self.__bool_setter(self.opt_coloroutput, use)

    @property
    def app_package(self):
        return self.__bool_getter(self.opt_coloroutput)

    @app_package.setter
    def app_package(self, use):
        self.__bool_setter(self.opt_coloroutput, use)

    @property
    def app_activity(self):
        return self.__bool_getter(self.opt_coloroutput)

    @app_activity.setter
    def app_activity(self, use):
        self.__bool_setter(self.opt_coloroutput, use)

    @property
    def app_wait_activity(self):
        return self.__bool_getter(self.opt_coloroutput)

    @app_wait_activity.setter
    def app_wait_activity(self, use):
        self.__bool_setter(self.opt_coloroutput, use)

    # Device options
    @property
    def device_ready_timeout(self):
        return self.__bool_getter(self.opt_coloroutput)

    @device_ready_timeout.setter
    def device_ready_timeout(self, use):
        self.__bool_setter(self.opt_coloroutput, use)

    @property
    def device_name(self):
        return self.__bool_getter(self.opt_coloroutput)

    @device_name.setter
    def device_name(self, use):
        self.__bool_setter(self.opt_coloroutput, use)
