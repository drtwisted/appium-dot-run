__author__ = 'twisted'
from models.options.option import Option
from structures.ui_options_groups import SETTINGS_GROUPS

class Options(object):
    def __init__(self, ui, config_reference):
        self.__list = dict()
        self.__ui = ui
        self.__config = config_reference

        self.__populate_options()

    def __populate_options(self):
        # print('opts: {}'.format(dict(self.__config.opt)))
        for option_name in dict(self.__config.opt):
            # print('OptionName: {}'.format(option_name))
            self.__list[option_name] = Option(self.__ui, option_name,
                                              self.__config)

    def __getitem__(self, item):
        return self.__list[item]

    def __setitem__(self, key, value):
        self.__list[key] = value

    def __iter__(self):
        for option_name in list(self.__config.opt):
            yield self.__getitem__(option_name)
1