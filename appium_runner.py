#!/usr/bin/python
__author__ = 'twisted'

import settings
import sys

from json import loads, dumps
from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL

from about_dlg import AboutDlg
from models.main_window import Ui_MainWindow
from models.config_handler import AppiumRunnerConfig
from models.command_runner import CommandRunner
from models.output_reader import OutputReader


class AppiumRunner(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Hide settings before we start
        self.__hide_settings()

        self.config = AppiumRunnerConfig(settings.CONFIG_PATH)
        self.__read_config()

        # Button signals connections
        self.ui.btnRun.clicked.connect(self.btnRun_clicked)
        self.ui.btnClear.clicked.connect(self.btnClear_clicked)
        self.ui.btnSettings.clicked.connect(self.btnSettings_clicked)
        self.ui.btnCancel.clicked.connect(self.btnCancel_clicked)
        self.ui.btnAbout.clicked.connect(self.btnAbout_clicked)
        self.ui.btnBrowseAppiumLocation.clicked.connect(
            self.btnBrowseAppiumLocation_clicked)

        self.running = False

    def __hide_settings(self):
        self.ui.frmSettings.setVisible(False)
        self.ui.btnCancel.setVisible(False)

    def __populate_modes_combobox(self):
        index, info_index = 0, 0
        log_levels = settings.LogLevel.__dict__

        self.ui.cmbOutputMode.clear()

        for level in sorted(log_levels.keys()):
            if level[:2] != '__':
                if level.lower() == self.config.log_level:
                    info_index = index
                self.ui.cmbOutputMode.addItem(log_levels[level])
                index += 1

        self.ui.cmbOutputMode.setCurrentIndex(info_index)

    def __read_config(self):
        self.ui.leAppiumLocation.setText(self.config.appium_location)
        self.ui.cbShowTimeStamp.setChecked(self.config.time_stamp)
        self.ui.cbColorOutput.setChecked(self.config.color_output)
        self.__populate_modes_combobox()

    def __save_config(self):
        self.config.appium_location = self.ui.leAppiumLocation.text()
        self.config.log_level = self.ui.cmbOutputMode.currentText()
        self.config.time_stamp = self.ui.cbShowTimeStamp.isChecked()
        self.config.color_output = self.ui.cbColorOutput.isChecked()
        self.config.save()

    def __collect_appium_options(self):
        options = (settings.AppiumOptions.TIME_STAMP
                   if self.ui.cbShowTimeStamp.isChecked() else '')
        options += settings.AppiumOptions.DEFAULT_OPTIONS
        options += settings.AppiumOptions.LOG_LEVEL_TEMPLATE.format(
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

        self.cmdr = CommandRunner(
            ['{} {} {}'.format(settings.NODE, cmd, options)])
        self.cmdr.run()
        self.ui.teOutput.append('>> Starting appium...')
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
        return str(
            QtGui.QFileDialog.getExistingDirectory(
                self,
                caption='Select Appium directory',
                options=QtGui.QFileDialog.ShowDirsOnly))

    @staticmethod
    def __parse_output(text, color=False):
        _template = '>> {}: {} - {}'
        _color = '<font color={color}>{}</font>'
        _red = _color.format(color='"red"')
        _green = _color.format(color='"green"')
        _blue = _color.format(color='"blue"')
        _gray = _color.format(color='"gray"')
        _type = text[26:30]

        if color:
            if _type == settings.LogLevel.INFO:
                _type = _green.format(_type)
            elif _type == settings.LogLevel.ERROR:
                _type = _red.format(_type)
            elif _type == settings.LogLevel.DEBUG:
                _type = _blue.format(_type)
            return _template.format(
                _type, text[:23], _gray.format(text[32:]))
        else:
            return _template.format(_type, text[:23], text[32:])

    def _print_output(self, text):
        print('text: {}'.format(text))
        color = '<font color={color}>{ender}'
        ender = '{}</font>'
        red = color.format(color='"red"', ender=ender)
        yellow = color.format(color='"yellow"', ender=ender)
        orange = color.format(color='"orange"', ender=ender)
        lime = color.format(color='"lime"', ender=ender)
        green = color.format(color='"forestgreen"', ender=ender)
        teal = color.format(color='"teal"', ender=ender)
        ligth_steel_blue = color.format(color='"lightsteelblue"', ender=ender)

        def parse_json(message):
            do_format = False

            def found(res):
                return res >= 0

            def find_json_margin(text, end=False):
                def get_bigger(first, second):
                    if first > second:
                        return first
                    else:
                        return second

                opened = ('{', '[')
                closed = (']', '}')

                if end:
                    text_to_find = closed
                else:
                    text_to_find = opened

                first_priority_pos = text.find(text_to_find[0])
                second_priority_pos = text.find(text_to_find[1])

                if found(first_priority_pos) and found(second_priority_pos):
                    return get_bigger(first_priority_pos, second_priority_pos)
                else:
                    if found(first_priority_pos):
                        return first_priority_pos
                    elif found(second_priority_pos):
                        return second_priority_pos
                    else:
                        return -1

            json_start = find_json_margin(message)
            if found(json_start):
                json_end = find_json_margin(message, end=True)
                if found(json_end):
                    do_format = True

            if do_format:
                return '{pre}<br/>{JSON}{rest}'.format(
                    pre=message[:json_start],
                    JSON=dumps(
                        loads(message[json_start:json_end + 1]),
                        indent=2,
                        separators=(',', ': ')
                    ).replace('\n', '<br/>').replace(' ' * 2, '&nbsp;' * 2),
                    rest=message[json_end + 1:])
            else:
                return message

        def parse_request(message, _color=False):
            send_id = '<--'
            send_text = 'SEND&gt;'
            receive_id = '-->'
            receive_text = 'RECV&lt;'

            if _color:
                send = lime.format(send_text)
                receive = orange.format(receive_text)
            else:
                send = send_text
                receive = receive_text

            message = (
                message.replace(send_id, send)
                if send_id in message
                else message.replace(receive_id, receive)
                if receive_id in message else message)

            return message

        def parse_output(_text, _color=False):
            DEBUG_TYPE = 'debg'
            template = '>> {}: {} - {}'
            date_n_time = _text[:23]
            message_flag = _text[33:38]
            _type = _text[26:30]

            if message_flag == settings.LogLevel.DEBUG:
                _type = message_flag
                message = _text[40:]
            else:
                message = _text[32:]

            message = parse_request(message, _color=_color)
            message = parse_json(message)

            if _color:
                if _type == settings.LogLevel.INFO:
                    _type = green.format(_type)
                elif _type == settings.LogLevel.ERROR:
                    _type = red.format(_type)
                elif _type == settings.LogLevel.WARN:
                    _type == yellow.foramt(_type)
                elif _type == settings.LogLevel.DEBUG:
                    _type = teal.format(DEBUG_TYPE)
                report_string = template.format(
                    _type, date_n_time, ligth_steel_blue.format(
                        parse_request(message, _color=_color)))
            else:
                report_string =  template.format(_type, date_n_time, message)

            return report_string

        __text = parse_output(text, _color=self.ui.cbColorOutput.isChecked())
        # decorator = '-' * 20
        # print(decorator + '\nFORMATED: \n{}\n'.format(__text) + decorator)

        self.ui.teOutput.append(__text)

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

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    appium_runner = AppiumRunner()
    appium_runner.show()
    _res = app.exec_()
    appium_runner.clean_up()
    sys.exit(_res)
