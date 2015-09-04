__author__ = 'twisted'

from threading import Thread
from subprocess import Popen, PIPE


class CommandRunner(Thread):
    def __init__(self, command=[]):
        Thread.__init__(self)
        self.command = command
        self.__process = None

    def get_process(self):
        return self.__process

    def run(self):
        self.__process = Popen(self.command, stdout=PIPE, stderr=PIPE,
                               shell=True)

    def stop(self):
        if self.__process:
            self.__process.kill()
            self.__process = None
