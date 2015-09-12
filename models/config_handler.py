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

# TODO: Create generator for options

# TODO: Setter/Getter for Yes/No options, do something about ComboBoxes

class AppiumRunnerConfig(ConfigHandler):
    def __init__(self, config_path):
        ConfigHandler.__init__(self, config_path=config_path)
        self.__identity = 'appiumrunner'
        self.opt = dict()
        self.opt['AppiumLocation'] = ('appium_location', str)
        
        # Log options
        self.opt['LogLevel'] = ('log_level', str)
        # self.opt['TimeStamp'] = ('time_stamp', bool)
        self.opt['ColorOutput'] = ('color_output', bool)
        # self.opt['UseLocalTimezone'] = ('use_local_timezone', bool)
        # self.opt['WriteToLog'] = ('write_to_log', bool)
        self.opt['LogPath'] = ('log_path', str)

        # Server options
        # self.opt['ShowStartupCommand'] = ('show_startup_command', bool)
        self.opt['ServerAddress'] = ('server_address', str)
        self.opt['ServerPort'] = ('server_port', str)
        self.opt['CommandTimeout'] = ('command_timeout', int)

        # Test application options
        self.opt['AppPath'] = ('app_path', str)
        # self.opt['AppNoReset'] = ('app_no_reset', bool)
        self.opt['AppPackage'] = ('app_package', str)
        self.opt['AppActivity'] = ('app_activity', str)
        self.opt['AppWaitActivity'] = ('app_wait_activity', str)

        # Device options
        self.opt['DeviceReadyTimeout'] = ('device_ready_timeout', int)
        self.opt['DeviceName'] = ('device_name', str)

        self.__generate_config_options()

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

    def __generate_config_options(self):
        def __generate_set_method(name, _type):
            if _type == bool:
                def _setter(_val):
                    self.__bool_setter(name, _val)
            elif _type == str or _type == int:
                def _setter(_val):
                    self.set(self.__identity, name, str(_val))
            else:
                _setter = None

            return _setter

        def __generate_get_method(name, _type):
            if _type == bool:
                def _getter():
                    return self.__bool_getter(name)
            elif _type == str:
                def _getter():
                    _res = self.get(self.__identity, name, fallback='')
                    # if _res is not None:
                    #     return tuple(True, str(_res))
                    # else:
                    #     return tuple(False, )
                    return _res
            elif _type == int:
                def _getter():
                    try:
                        _res = int(self.get(self.__identity, name, fallback=0))
                    except ValueError:
                        _res = 0
                    return int(_res)
            else:
                _getter = None

            return _getter

        def __generate_del_method(name):
            def deleter():
                try:
                    self[self.__identity].pop(name)
                    return True
                except KeyError:
                    return False

            return deleter

        for option_name in self.opt.keys():
            option_method_name, option_type = self.opt[option_name]
            # print('option: {}'.format(option_method_name))
            setattr(self, 'set_{}'.format(option_method_name),
                    __generate_set_method(option_method_name, option_type))
            # get_method = __generate_get_method(option_method_name, option_type)
            # setattr(self, 'with_{}'.format(option_method_name)
            #         if option_type == bool else option_method_name,
            #         __generate_get_method(option_method_name, option_type))
            setattr(self, option_method_name,
                    __generate_get_method(option_method_name, option_type))
            setattr(self, 'del_{}'.format(option_method_name),
                    __generate_del_method(option_method_name))

    @property
    def is_valid(self):
        return self.__identity in self.sections()


    def with_time_stamp(self):
        return self.__bool_getter('time_stamp')

    def set_time_stamp(self, show):
        self.__bool_setter('time_stamp', show)

    def with_color_output(self):
        return self.__bool_getter('color_output')

    def set_color_output(self, use):
        self.__bool_setter('color_output', use)

# For testing
if __name__ == '__main__':
    a = AppiumRunnerConfig('./config.ini')