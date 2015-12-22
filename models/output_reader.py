__author__ = 'twisted'
from PyQt4 import QtCore

class OutputReader(QtCore.QThread):
    def __init__(self, cmd_runner=None, _callback_object=None):
        QtCore.QThread.__init__(self)
        self.__cmdr = None
        self.__callback_object = None
        self.set_command_runner(cmd_runner)
        self.set_output_callback_object(_callback_object)
        self.__stop = False

    def set_command_runner(self, cmd_runner):
        self.__cmdr = cmd_runner

    # obsolete
    def set_output_callback_object(self, _callback_object):
        self.__callback_object = _callback_object

    def run(self):
        if self.__cmdr is not None:
            self.__stop = False
            while not self.__stop:
                line = (
                    self.__cmdr.get_process()
                        .stdout.readline().decode().replace('\n', ''))

                if str(line) != '':
                    self.emit(QtCore.SIGNAL('update(QString)'),
                              line)
            self.__cmdr.stop()

    def stop(self):
        self.__stop = True
