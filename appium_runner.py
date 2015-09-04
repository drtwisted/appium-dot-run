#!/usr/bin/python
__author__ = 'twisted'

import settings
import sys

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL

from models.main_window import Ui_MainWindow
from models.command_runner import CommandRunner
from models.output_reader import OutputReader


class AppiumRunner(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnRun.clicked.connect(self.btnRun_clicked)
        self.ui.leCmd.setText(settings.CMD)
        self.running = False

    def __get_output(text):
        pass

    def _print_output(self, text):
        self.ui.teOutput.append(text)

    def _clear_output(self):
        self.ui.teOutput.clear()

    def __start_appium(self):
        self.cmdr = CommandRunner([self.ui.leCmd.text()])
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
        self.ui.teOutput.append('>> Appium STOPED.')
        self.running = False

    def btnRun_clicked(self):
        if not self.running:
            self.__start_appium()
        else:
            self.__kill_appium()

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