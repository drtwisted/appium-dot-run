__author__ = 'twisted'

from PyQt4 import QtGui
from models.about_dialog import Ui_dlgAbout


class AboutDlg(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.ui = Ui_dlgAbout()
        self.ui.setupUi(self)
        self.ui.btnOk.clicked.connect(self.btnOk_clicked)

    def btnOk_clicked(self):
        self.close()