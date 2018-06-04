# -*- coding: utf-8 -*-

# 学习对象：https://blog.csdn.net/liang19890820

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

Theme = """"""


class TitleBar(QtWidgets.QMainWindow):
    def __init__(self):
        super(TitleBar, self).__init__()

        """虾米音乐"""
        """最大化，最小化，关闭按键"""
        """用户按键"""





class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        # 学习的对象：https://blog.csdn.net/liang19890820/article/details/50357523

        """ 定义变量, 在这里继承了父类：widget """
        self.pushButton = QtWidgets.QPushButton(Form)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.layout = QtWidgets.QHBoxLayout(Form)

        """ 当鼠标放到按键上，鼠标的箭头变为手型 """
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        """ 接上条，鼠标的箭头变为手型后，给出文字提示 """
        self.pushButton.setToolTip(str("search"))

        # url的根目录./是main.py所在的目录！！！！！
        """ qss（qt style sheet）定义按键的属性"""
        add = """
        QPushButton
        {
            max-width: 18px;
            max-height: 18px;
            border-image: url("./ui/icon/1.png");
            background:transparent;
        }
        QPushButton:hover
        {
            border-image: url("./ui/icon/2.png");
        }
        QPushButton:pressed
        {
            border-image: url("./ui/icon/3.png");
        }
        """
        self.pushButton.setStyleSheet(add)

        """ 设置用户看到的按键名字，就是在按键上写名字 """
        self.pushButton.setText("")

        """ 设置按键的名字，qss可以使用 """
        self.pushButton.setObjectName("pushButton")

        """ 设置按键的位置 """
        # self.pushButton.setGeometry(QtCore.QRect(80, 90, 15, 15))

        # box module，所有的组件组成的模式！！！！！！！！很重要:
        # http://doc.qt.io/qt-5/stylesheet-customizing.html
        """ 获取输入框的透明区域 """
        self.Margins = self.lineEdit.textMargins()

        """
        将lineEdit的右边透明区域(margins)设置为按键宽度，减少输入空间，留给按键显示
        因为按键宽度是在qss控制的，所以self.pushButton.width()获取的宽度100是不对的，直接手动填入宽度18
        """
        self.lineEdit.setTextMargins(self.Margins.left(), self.Margins.top(), 18, self.Margins.bottom())

        """ 输入框提示 """
        self.lineEdit.setPlaceholderText(str("please input"))

        """ 如果输入的是密码不想显示输入字符 """
        self.lineEdit.setEchoMode(2)

        """setSpacing：设置组件和组件的间隔"""
        self.layout.setSpacing(0)

        """setContentsMargins：设置layout边框到组件的空白距离"""
        self.layout.setContentsMargins(0, 0, 0, 0)

        """
        https://blog.csdn.net/liang19890820/article/details/51537246
        对齐
        https://www.jianshu.com/p/bab37cdac844
        """
        self.layout.addStretch()
        self.layout.addWidget(self.pushButton)

        """
        setlayout对组件布局:
        https://blog.csdn.net/groundhappy/article/details/52020779
        qtdesiner使用的第一种
        """
        self.lineEdit.setLayout(self.layout)

        # self.pushButton.setLayout(self.layout)
        # self.lineEdit.setGeometry(QtCore.QRect(0, 0, 100, 15))

        """ 调用lineEdit函数实现搜索栏和搜索事件
        https://blog.csdn.net/rl529014/article/details/52060373"""
        # self.action1 = QtWidgets.QAction()
        # self.action1.setIcon(QIcon("./ui/icon/1.png"))
        # self.lineEdit.addAction(self.action1, 2)
        # 只添加图标
        # self.lineEdit.addAction(QIcon("./ui/icon/1.png"), 2)
        # self.action1.triggered["bool"].connect(self.process)

        # 按键信号处理
        self.pushButton.clicked['bool'].connect(self.process)
        # self.pushButton.clicked.connect(self.process)


    def process(self):
        self.strText = self.lineEdit.text()

        # print(type(self.strText))
        # 'str' object has no attribute 'isEmpty'
        # 所以直接使用self.strText判断
        try:
            if self.strText:
                print(self.strText)
            else:
                print("oh no")

        except Exception as e:
            print("error:" + str(e))
