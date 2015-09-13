__author__ = 'twisted'
from helpers.setting_toggle import set_widgets_visible_state
from structures.ui_options_groups import SETTINGS_GROUPS


class Classss(object):
    def __init__(self):
        self.param1, self.param2 = 1, '2'

    def __dummy(self):
        pass

    def dummy(self):
        pass

    def _dummy(self):
        pass


class Option(object):
    def __init__(self, ui, name, config_reference):
        print('Creating {}'.format(name))
        self.__config = config_reference
        self.__name = name
        self.__method_name, self.__type = self.__config.opt[self.__name]
        self.__ui = ui
        self.__container, self.__sidekicks \
            = self.__get_value_container_and_sidekicks()
        self.checkbox = getattr(self.__ui, 'cb{}'.format(self.__name), None)
        if self.__container is None:
            self.__container = self.checkbox
        self.value = None
        self.__generate_option_toggler()
        # self.update_state()

    def __generate_method(self):
            def _clicked():
                set_widgets_visible_state(self.__ui, self.__name,
                                          self.checkbox.isChecked())
            return _clicked

    def __generate_option_toggler(self):
        if self.checkbox:
            self.checkbox.clicked.connect(
                self.__generate_method())

    def __get_value_container_and_sidekicks(self):
        container, sidekicks = None, list()
        for prefix in ('le', 'sb', 'lb', 'cb'):
            try:
                element = getattr(self.__ui,
                                   '{}{}'.format(prefix, self.__name))
                if not container:
                    container = element
                else:
                    sidekicks.append(element)
                # print('Container: {}'.format(container.__name__))
                return container, sidekicks
            except AttributeError:
                # print('No {} container for {}'.format(prefix, self.__name))
                pass

        return None

    def __enable_elements(self):
        try:
            self.checkbox.setChecked(True)
            for element in self.__sidekicks + [self.__container]:
                element.setEnabled(True)
        except AttributeError:
            print('Could not enable elemtnts of {}'.format(self.__method_name))

    def __update_state(self, state):
        if self.checkbox:
            self.checkbox.setChecked(state)

    def set_state_(self, state):
        self.checkbox.setChecked(state)

    def update_state(self):
        self.__update_state(self.enabled)

    def update_value(self):
        self.value = self.__container.text() if self.__container else None
        return self

    def read_value(self):
        type_methods = {int: 'setValue', str: 'setText', bool: 'setChecked'}

        print('Trying to find getter: {}'.format(self.__method_name))
        getter = getattr(self.__config, self.__method_name)
        if hasattr(getter, '__call__'):
            value = getter()

            try:
                value = self.__type(value)
                print('{} value set'.format(self.__method_name))
                try:   # Set value with corresponding method, see type_methods dict
                    try:
                        getattr(self.__container, type_methods.get(
                            self.__type))(value)
                        self.__enable_elements()
                        print('Set value in ui')
                    except IndexError:
                        print('Cant set value of type {}'.format(self.__type))
                except AttributeError:
                    print('Failed to set {} value {} for {}'.format(
                        self.__type, value, self.__container))
            except ValueError:
                print(
                    '{} parameter value {} is invalid.'.format(
                        self.__method_name,
                        value) + ' Should be of {} type'.format(
                        str(self.__type)))

        else:
            print('{} is not callable, cant get value for {}'.format(
                getter, self.__method_name))



        # TODO: work with bool

    @property
    def enabled(self):
        # print('value is: {}'.format(str(self.value is not None)))
        return self.value is not None and self.value != ''

    def load(self):
        """
        Load from settings
        :return:
        """
        print('Getting value for {}'.format(self.__method_name))

        self.read_value()
        self.update_state()
        # _res = None
        # try:
        #     _res = getattr(self.__config, self.__method_name)()
        # except TypeError:
        #     print('Type error with {}'.format(self.__method_name))
        #
        # if isinstance(_res, str) or isinstance(_res, int) \
        #         or isinstance(_res, bool):
        #     self.value = _res
        # else:
        #     print('No valid value to load for {}'.format(self.__method_name))

    def save_(self):
        """
        Save from settings
        :return:
        """
        value = ''
        chck_box = self.checkbox
        method = self.__method_name
        container = self.__container

        if self.checkbox:
            if self.checkbox == self.__container:
                value = self.__container.isChecked()
            elif self.checkbox.isChecked():
                value = self.value
        else:
            if self.__container:
                value = self.__container.text()

        getattr(self.__config, 'set_{}'.format(self.__method_name))(value)

        # if chck_box or self.value:
        #     if self.__container and (chck_box and chck_box.isChecked()):
        #         value = self.value
        #     elif not self.value:
        #         value = chck_box.isChecked()
        #
        #     if value is not None:
        #         getattr(self.__config,
        #                 'set_{}'.format(self.__method_name))(value)
        #     else:
        #         print('No value to set for {}'.format(self.__method_name))
        #
        # else:
        #     print('No checkbox for {}'.format(self.__method_name))

    def save(self, value):
        self.value = value
        self.save_()
