# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.py'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from untitled import *
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
FRONTEND = os.path.abspath(os.path.join(ABSPATH, sys.argv[0]))
print(ABSPATH + "\\ui")
sys.path.append(ABSPATH + "\\ui")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UiInit()
    sys.exit(app.exec_())