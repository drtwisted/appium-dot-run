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

    def __get_output(text):
        pass

    def _print_output(self, text):
        self.ui.teOutput.append(text)

    def btnRun_clicked(self):
        self.ui.leCmd.setText(str(settings.CMD))
        self.cmdr = CommandRunner([settings.CMD])
        self.cmdr.run()
        self.reader = OutputReader(self.cmdr, self.ui.teOutput)
        self.connect(self.reader, SIGNAL("update(QString)"),
                     self._print_output)
        self.reader.start()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    appium_runner = AppiumRunner()
    appium_runner.show()
    sys.exit(app.exec_())