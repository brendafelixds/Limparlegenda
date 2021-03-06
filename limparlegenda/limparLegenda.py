# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\limparLegenda.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QHBoxLayout, QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 309)
        MainWindow.setMinimumSize(QtCore.QSize(697, 309))
        MainWindow.setMaximumSize(QtCore.QSize(697, 309))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icons8-subtitles-26.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("font: 75 11pt \"Ubuntu\";\n"
"image: url(:/newPrefix/scale.jpeg);\n"
"background-color: rgb(0, 0, 0);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 210, 131, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Ubuntu\";\n"
"font: 75 11pt \"Ubuntu Condensed\";")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(120, 140, 451, 51))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(478, 145, 91, 40))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("image: url(:/newPrefix/icons8-add-folder-64.png);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 71, 61))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(:/newPrefix/icons8-subtitles-26.png);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Ubuntu\";\n"
"font: 75 11pt \"Ubuntu Mono\";\n"
"font: 75 14pt \"Ubuntu Condensed\";\n"
"image: url(:/newPrefix/icons8-baby-yoda-50.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(121, 112, 91, 17))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(118, 278, 451, 20))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Condensed\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Limpar Legenda by Rafael & Brenda"))
        self.pushButton.setText(_translate("MainWindow", "LIMPAR"))
        self.label_3.setText(_translate("MainWindow", "Arquivo srt:"))
        self.label_4.setText(_translate("MainWindow", "made by Rafael & Brenda :)"))
        self.pushButton.clicked.connect(self.console)
     
    def console(self):
     widget = QWidget()   
     option = QFileDialog.Options()
     file = QFileDialog.getOpenFileName(widget, "Open Single File", "Default File", "All Files(*)", options=option)
     self.lineEdit.setText(file[0])

import img3_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
