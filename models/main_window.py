# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'models/main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(894, 682)
        MainWindow.setStyleSheet(_fromUtf8(".QTextEdit\n"
"{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 26, 47, 255), stop:0.55 rgba(24, 42, 69, 255), stop:0.985 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"background-image: url(:/img/appium_logo_rgb.png);\n"
"background-repeat: no-repeat;\n"
"background-position: right bottom;\n"
"background-attachment: fixed;\n"
"color: rgb(231, 231, 231);\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.leCmd = QtGui.QLineEdit(self.centralwidget)
        self.leCmd.setObjectName(_fromUtf8("leCmd"))
        self.horizontalLayout.addWidget(self.leCmd)
        self.btnRun = QtGui.QPushButton(self.centralwidget)
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.horizontalLayout.addWidget(self.btnRun)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.teOutput = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(12)
        self.teOutput.setFont(font)
        self.teOutput.setReadOnly(True)
        self.teOutput.setObjectName(_fromUtf8("teOutput"))
        self.verticalLayout.addWidget(self.teOutput)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.lbStatus = QtGui.QLabel(self.centralwidget)
        self.lbStatus.setObjectName(_fromUtf8("lbStatus"))
        self.gridLayout_2.addWidget(self.lbStatus, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Appium Runner", None))
        self.btnRun.setText(_translate("MainWindow", "Run", None))
        self.teOutput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell\'; font-size:11pt;\"><br /></p></body></html>", None))
        self.lbStatus.setText(_translate("MainWindow", "Idle.", None))

import resources_rc
