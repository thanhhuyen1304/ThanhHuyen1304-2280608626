# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_C(object):
    def setupUi(self, C):
        C.setObjectName("C")
        C.resize(800, 599)
        C.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(C)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 60, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 130, 571, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(160, 220, 571, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(160, 270, 571, 71))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 290, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(210, 380, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_encrypt.setFont(font)
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(440, 380, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_decrypt.setFont(font)
        self.btn_decrypt.setObjectName("btn_decrypt")
        C.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(C)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menuBar.setObjectName("menuBar")
        C.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(C)
        self.statusbar.setObjectName("statusbar")
        C.setStatusBar(self.statusbar)

        self.retranslateUi(C)
        QtCore.QMetaObject.connectSlotsByName(C)

    def retranslateUi(self, C):
        _translate = QtCore.QCoreApplication.translate
        C.setWindowTitle(_translate("C", "Caesar Cipher"))
        self.label.setText(_translate("C", "CAESAR CIPHER"))
        self.label_2.setText(_translate("C", "Plain Text:"))
        self.label_3.setText(_translate("C", "Key:"))
        self.label_4.setText(_translate("C", "Cipher Text:"))
        self.btn_encrypt.setText(_translate("C", "Encrypt"))
        self.btn_decrypt.setText(_translate("C", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    C = QtWidgets.QMainWindow()
    ui = Ui_C()
    ui.setupUi(C)
    C.show()
    sys.exit(app.exec_())
