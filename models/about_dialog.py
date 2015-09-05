# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'models/about_dialog.ui'
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

class Ui_dlgAbout(object):
    def setupUi(self, dlgAbout):
        dlgAbout.setObjectName(_fromUtf8("dlgAbout"))
        dlgAbout.setWindowModality(QtCore.Qt.WindowModal)
        dlgAbout.resize(400, 260)
        dlgAbout.setSizeGripEnabled(True)
        self.graphicsView = QtGui.QGraphicsView(dlgAbout)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 381, 91))
        self.graphicsView.setStyleSheet(_fromUtf8("QGraphicsView {\n"
"background-image: url(:/img/appium_logo_rgb.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}"))
        self.graphicsView.setFrameShape(QtGui.QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QtGui.QFrame.Plain)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.lbRunnerTitle = QtGui.QLabel(dlgAbout)
        self.lbRunnerTitle.setGeometry(QtCore.QRect(227, 72, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lbRunnerTitle.setFont(font)
        self.lbRunnerTitle.setObjectName(_fromUtf8("lbRunnerTitle"))
        self.lbVersion = QtGui.QLabel(dlgAbout)
        self.lbVersion.setGeometry(QtCore.QRect(330, 27, 66, 21))
        self.lbVersion.setObjectName(_fromUtf8("lbVersion"))
        self.textBrowser = QtGui.QTextBrowser(dlgAbout)
        self.textBrowser.setGeometry(QtCore.QRect(4, 110, 391, 111))
        self.textBrowser.setFrameShape(QtGui.QFrame.WinPanel)
        self.textBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.btnOk = QtGui.QPushButton(dlgAbout)
        self.btnOk.setGeometry(QtCore.QRect(308, 227, 87, 30))
        self.btnOk.setObjectName(_fromUtf8("btnOk"))

        self.retranslateUi(dlgAbout)
        QtCore.QMetaObject.connectSlotsByName(dlgAbout)

    def retranslateUi(self, dlgAbout):
        dlgAbout.setWindowTitle(_translate("dlgAbout", "Dialog", None))
        self.lbRunnerTitle.setText(_translate("dlgAbout", "runner", None))
        self.lbVersion.setText(_translate("dlgAbout", "v0.2", None))
        self.textBrowser.setHtml(_translate("dlgAbout", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Authors:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\"> - Kirill Omelchenko [kirill.omelchenko@gmail.com]<br /><br /></span></p></body></html>", None))
        self.btnOk.setText(_translate("dlgAbout", "OK", None))

import resources.resources_rc
