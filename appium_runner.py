#!/usr/bin/python
import structures.options

__author__ = 'twisted'

import settings
import sys

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL

from about_dlg import AboutDlg
from helpers.setting_toggle import set_widgets_visible_state
from models.main_window import Ui_MainWindow
from models.config_handler import AppiumRunnerConfig
from models.command_runner import CommandRunner
from models.output_reader import OutputReader
from models.options.options import Options
from structures.ui_options_groups import SETTINGS_GROUPS


class AppiumRunner(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Hide settings before we start
        self.__hide_settings()

        self.config = AppiumRunnerConfig(settings.CONFIG_PATH)
        self.options_groups = Options(self.ui, self.config)
        self.__read_config()

        # Button signals connections
        self.ui.btnRun.clicked.connect(self.btnRun_clicked)
        self.ui.btnClear.clicked.connect(self.btnClear_clicked)
        self.ui.btnSettings.clicked.connect(self.btnSettings_clicked)
        self.ui.btnCancel.clicked.connect(self.btnCancel_clicked)
        self.ui.btnAbout.clicked.connect(self.btnAbout_clicked)
        self.ui.btnBrowseAppiumLocation.clicked.connect(
            self.btnBrowseAppiumLocation_clicked)


        # Settings Checkboxes
        # self.ui.cbAppPath.clicked.connect(self.cbAppPath_clicked)
        # self.__generate_settings_togglers()

        # for item in self.config.__dict__:
        #     print('{}: {}'.format(item, self.config.__dict__[item]))

        self.running = False

    # def __generate_settings_togglers(self):
    #     def generate_method(_self, name, _check_box):
    #         def _clicked():
    #             set_widgets_visible_state(_self.ui, name,
    #                               _check_box.isChecked())
    #         return _clicked
    #
    #     for option in self.config.opt.keys():
    #         check_box = getattr(self.ui, 'cb{}'.format(option), None)
    #         if check_box:
    #             check_box.clicked.connect(
    #                 generate_method(self, option, check_box))

    #Settings Checkbuttons
    # def cbAppPath_clicked(self):
    #     set_widgets_visible_state(self.ui, SettingsGroups.app_path,
    #                               self.ui.cbAppPath.isChecked())

    def __hide_settings(self):
        self.ui.frmSettings.setVisible(False)
        self.ui.btnCancel.setVisible(False)

    def __populate_modes_combobox(self):
        index, info_index = 0, 0
        # TODO: Replace with ordinary dictionary
        log_levels = structures.options.LogLevel.__dict__

        self.ui.cmbOutputMode.clear()

        for level in sorted(log_levels.keys()):
            if level[:2] != '__':
                if level.lower() == self.config.log_level():
                    info_index = index
                self.ui.cmbOutputMode.addItem(log_levels[level])
                index += 1

        self.ui.cmbOutputMode.setCurrentIndex(info_index)

    def __read_config(self):
        for option_group in self.options_groups:
            option_group.load()
        # self.ui.leAppiumLocation.setText(self.config.appium_location())
        # self.ui.cbShowTimeStamp.setChecked(self.config.with_time_stamp())
        # self.ui.cbColorOutput.setChecked(self.config.with_color_output())
        self.__populate_modes_combobox()

    def __save_config(self):
        for option_group in self.options_groups:
            option_group.update_value().save_()
        # self.config.set_appium_location(self.ui.leAppiumLocation.text())
        # self.config.set_log_level(self.ui.cmbOutputMode.currentText())
        # self.config.set_time_stamp(self.ui.cbShowTimeStamp.isChecked())
        # self.config.set_color_output(self.ui.cbColorOutput.isChecked())
        self.config.save()

    def __collect_appium_options(self):
        options = structures.options.AppiumOptions.TIME_STAMP \
            if self.ui.cbShowTimeStamp.isChecked() else ''
        options += structures.options.AppiumOptions.DEFAULT_OPTIONS
        options += structures.options.AppiumOptions.LOG_LEVEL_TEMPLATE.format(
            self.ui.cmbOutputMode.currentText())
        return options

    def __start_appium(self):
        options = self.__collect_appium_options()
        cmd = self.ui.leAppiumLocation.text()

        if not cmd or cmd == '':
            QtGui.QMessageBox.warning(self, 'Where is Appium?',
                                      'Appium location is not set. '
                                      'Go to Settings to set your '
                                      'Appium installation location.')
            return

        appium_startup_cmd = '{} {} {}'.format(settings.NODE, cmd, options)
        self.cmdr = CommandRunner([appium_startup_cmd])
        self.cmdr.run()
        self.ui.teOutput.append('>> Starting appium...')
        self.ui.teOutput.append('   {}'.format(appium_startup_cmd))
        self.reader = OutputReader(self.cmdr, self.ui.teOutput)
        self.connect(self.reader, SIGNAL("update(QString)"),
                     self._print_output)
        self.reader.start()
        self.ui.btnRun.setText('Stop')
        self.ui.lbStatus.setText('Running...')
        self.running = True

    def __kill_appium(self):
        self.reader.stop()
        self.cmdr.stop()
        # self._clear_output()
        self.ui.btnRun.setText('Run')
        self.ui.lbStatus.setText('Stopped. Idle.')
        self.ui.teOutput.append('>> Appium STOPPED.')
        self.running = False

    def __select_appium_dir(self):
        return str(QtGui.QFileDialog.getExistingDirectory(
            self, caption='Select Appium directory',
            options=QtGui.QFileDialog.ShowDirsOnly))

    def _print_output(self, text):

        # print('received text:\n{}'.format(text))

        def parse_output(_text, color=False):
            template = '>> {}: {} - {}'
            _color = '<font color={color}>{ender}'
            ender = '{}</font>'
            red = _color.format(color='"red"', ender=ender)
            green = _color.format(color='"green"', ender=ender)
            blue = _color.format(color='"blue"', ender=ender)
            gray = _color.format(color='"gray"', ender=ender)
            _time = _text[:23]
            _type = _text[26:30]
            message = _text[32:].replace('<', '&lt;').replace('>', '&gt;')

            if color:
                if _type == structures.options.LogLevel.INFO:
                    _type = green.format(_type)
                elif _type == structures.options.LogLevel.ERROR:
                    _type = red.format(_type)
                elif _type == structures.options.LogLevel.DEBUG:
                    _type = blue.format(_type)
                return template.format(
                    _type, _time, gray.format(message))
            else:
                return template.format(_type, _time, message)

        self.ui.teOutput.append(
            parse_output(text, color=self.ui.cbColorOutput.isChecked()))

    def _clear_output(self):
        self.ui.teOutput.clear()

    @property
    def settings_opened(self):
        return self.ui.frmSettings.isVisible()

    # Settings section
    def btnBrowseAppiumLocation_clicked(self):
        _dir = self.__select_appium_dir()
        if isinstance(_dir, str) and not _dir == '':
            self.ui.leAppiumLocation.setText(_dir)

    def btnRun_clicked(self):
        if not self.running:
            self.__start_appium()
        else:
            self.__kill_appium()

    def btnClear_clicked(self):
        self.ui.teOutput.clear()

    def btnSettings_clicked(self):
        self.ui.btnCancel.setVisible(not self.settings_opened)
        if self.settings_opened:
            self.ui.btnSettings.setText('Settings')
            self.__save_config()
        else:
            self.ui.btnSettings.setText('Save')
        self.ui.frmSettings.setVisible(not self.settings_opened)

    def btnCancel_clicked(self):
        self.ui.btnCancel.setVisible(False)
        self.ui.frmSettings.setVisible(False)
        self.ui.btnSettings.setText('Settings')
        self.__read_config()

    def btnAbout_clicked(self):
        about = AboutDlg(parent=self)
        about.show()

    def clean_up(self):
        if self.running:
            self.__kill_appium()

        self.ui.horizontalLayout.children()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    appium_runner = AppiumRunner()
    appium_runner.show()
    _res = app.exec_()
    appium_runner.clean_up()
    sys.exit(_res)
