# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class ControlBar(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ControlBar, self).__init__(parent)
        print("wen min")
        self.setupControlBar()
        self.show()

    def setupControlBar(self):
        self.setObjectName("ControlBar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.checkBox = QtWidgets.QCheckBox()
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_5.addWidget(self.checkBox)
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.checkBox_2 = QtWidgets.QCheckBox()
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_5.addWidget(self.checkBox_2)
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalSlider = QtWidgets.QSlider()
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.checkBox_3 = QtWidgets.QCheckBox()
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_5.addWidget(self.checkBox_3)
        self.label_6 = QtWidgets.QLabel()
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.checkBox_4 = QtWidgets.QCheckBox()
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_5.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox()
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_5.addWidget(self.checkBox_5)
        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.pushButton_7 = QtWidgets.QPushButton()
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.label_7 = QtWidgets.QLabel()
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.checkBox_6 = QtWidgets.QCheckBox()
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_5.addWidget(self.checkBox_6)
        self.raise_()

        self.file = QtCore.QFile("./qss/skin.qss")
        if file.open(QtCore.QFile.ReadOnly):
            self.styleSheet = str(file.readAll(), encoding='utf8')
            self.setStyleSheet(self.styleSheet)
