# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.py'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
# from ui.ui import Ui_Form
from test import Ui_Form
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
FRONTEND = os.path.abspath(os.path.join(ABSPATH, sys.argv[0]))

sys.path.append(ABSPATH + "ui")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
test