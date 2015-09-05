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
        MainWindow.setStyleSheet(_fromUtf8(".QButton#btnSettings{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(109, 140, 163, 255), stop:0.77665 rgba(74, 75, 59, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
".QGroupBox\n"
"{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(151, 151, 151, 64), stop:1 rgba(255, 255, 255, 0));\n"
"font: bold;\n"
"}\n"
".QLabel#lbSettings\n"
"{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(40, 61, 139, 255), stop:1 rgba(60, 23, 120, 134));\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
".QTextEdit\n"
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
        self.btnAbout = QtGui.QPushButton(self.centralwidget)
        self.btnAbout.setObjectName(_fromUtf8("btnAbout"))
        self.horizontalLayout.addWidget(self.btnAbout)
        self.btnSettings = QtGui.QPushButton(self.centralwidget)
        self.btnSettings.setDefault(False)
        self.btnSettings.setFlat(False)
        self.btnSettings.setObjectName(_fromUtf8("btnSettings"))
        self.horizontalLayout.addWidget(self.btnSettings)
        self.btnCancel = QtGui.QPushButton(self.centralwidget)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout.addWidget(self.btnCancel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnRun = QtGui.QPushButton(self.centralwidget)
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.horizontalLayout.addWidget(self.btnRun)
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy)
        self.btnClear.setMinimumSize(QtCore.QSize(0, 0))
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.horizontalLayout.addWidget(self.btnClear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.frmSettings = QtGui.QFrame(self.centralwidget)
        self.frmSettings.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmSettings.sizePolicy().hasHeightForWidth())
        self.frmSettings.setSizePolicy(sizePolicy)
        self.frmSettings.setMinimumSize(QtCore.QSize(0, 110))
        self.frmSettings.setObjectName(_fromUtf8("frmSettings"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frmSettings)
        self.gridLayout_3.setMargin(2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lbSettings = QtGui.QLabel(self.frmSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbSettings.sizePolicy().hasHeightForWidth())
        self.lbSettings.setSizePolicy(sizePolicy)
        self.lbSettings.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbSettings.setFont(font)
        self.lbSettings.setObjectName(_fromUtf8("lbSettings"))
        self.verticalLayout_2.addWidget(self.lbSettings)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.grpMainSettings = QtGui.QGroupBox(self.frmSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grpMainSettings.sizePolicy().hasHeightForWidth())
        self.grpMainSettings.setSizePolicy(sizePolicy)
        self.grpMainSettings.setMinimumSize(QtCore.QSize(0, 136))
        self.grpMainSettings.setObjectName(_fromUtf8("grpMainSettings"))
        self.layoutWidget = QtGui.QWidget(self.grpMainSettings)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 30, 301, 61))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lbAppiumLocation = QtGui.QLabel(self.layoutWidget)
        self.lbAppiumLocation.setObjectName(_fromUtf8("lbAppiumLocation"))
        self.verticalLayout_3.addWidget(self.lbAppiumLocation)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.leAppiumLocation = QtGui.QLineEdit(self.layoutWidget)
        self.leAppiumLocation.setMinimumSize(QtCore.QSize(0, 26))
        self.leAppiumLocation.setObjectName(_fromUtf8("leAppiumLocation"))
        self.horizontalLayout_3.addWidget(self.leAppiumLocation)
        self.btnBrowseAppiumLocation = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrowseAppiumLocation.sizePolicy().hasHeightForWidth())
        self.btnBrowseAppiumLocation.setSizePolicy(sizePolicy)
        self.btnBrowseAppiumLocation.setMinimumSize(QtCore.QSize(0, 26))
        self.btnBrowseAppiumLocation.setObjectName(_fromUtf8("btnBrowseAppiumLocation"))
        self.horizontalLayout_3.addWidget(self.btnBrowseAppiumLocation)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addWidget(self.grpMainSettings)
        self.grpOutputOptions = QtGui.QGroupBox(self.frmSettings)
        self.grpOutputOptions.setFlat(False)
        self.grpOutputOptions.setObjectName(_fromUtf8("grpOutputOptions"))
        self.cbShowTimeStamp = QtGui.QCheckBox(self.grpOutputOptions)
        self.cbShowTimeStamp.setGeometry(QtCore.QRect(10, 60, 125, 23))
        self.cbShowTimeStamp.setAutoFillBackground(False)
        self.cbShowTimeStamp.setObjectName(_fromUtf8("cbShowTimeStamp"))
        self.layoutWidget1 = QtGui.QWidget(self.grpOutputOptions)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 90, 165, 28))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lbOutputMode = QtGui.QLabel(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbOutputMode.sizePolicy().hasHeightForWidth())
        self.lbOutputMode.setSizePolicy(sizePolicy)
        self.lbOutputMode.setMinimumSize(QtCore.QSize(0, 24))
        self.lbOutputMode.setObjectName(_fromUtf8("lbOutputMode"))
        self.horizontalLayout_4.addWidget(self.lbOutputMode)
        self.cmbOutputMode = QtGui.QComboBox(self.layoutWidget1)
        self.cmbOutputMode.setMinimumSize(QtCore.QSize(0, 24))
        self.cmbOutputMode.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.cmbOutputMode.setObjectName(_fromUtf8("cmbOutputMode"))
        self.horizontalLayout_4.addWidget(self.cmbOutputMode)
        self.cbColorOutput = QtGui.QCheckBox(self.grpOutputOptions)
        self.cbColorOutput.setGeometry(QtCore.QRect(10, 30, 125, 23))
        self.cbColorOutput.setAutoFillBackground(False)
        self.cbColorOutput.setObjectName(_fromUtf8("cbColorOutput"))
        self.horizontalLayout_2.addWidget(self.grpOutputOptions)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frmSettings)
        self.teOutput = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(12)
        self.teOutput.setFont(font)
        self.teOutput.setReadOnly(True)
        self.teOutput.setHtml(_fromUtf8("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.teOutput.setAcceptRichText(True)
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
        self.btnAbout.setText(_translate("MainWindow", "About", None))
        self.btnSettings.setText(_translate("MainWindow", "Settings", None))
        self.btnCancel.setText(_translate("MainWindow", "Cancel", None))
        self.btnRun.setText(_translate("MainWindow", "Run", None))
        self.btnClear.setText(_translate("MainWindow", "Clear", None))
        self.lbSettings.setText(_translate("MainWindow", " Appium Settings", None))
        self.grpMainSettings.setTitle(_translate("MainWindow", "Main", None))
        self.lbAppiumLocation.setText(_translate("MainWindow", "Appium Location:", None))
        self.btnBrowseAppiumLocation.setText(_translate("MainWindow", "Browse", None))
        self.grpOutputOptions.setTitle(_translate("MainWindow", "Output options", None))
        self.cbShowTimeStamp.setText(_translate("MainWindow", "Show timestamp", None))
        self.lbOutputMode.setText(_translate("MainWindow", "Output Mode:", None))
        self.cbColorOutput.setText(_translate("MainWindow", "Color output", None))
        self.lbStatus.setText(_translate("MainWindow", "Idle.", None))

import resources.resources_rc
