# -*- coding: utf-8 -*-

'''
    【简介】
	PyQT5将窗口放在屏幕中间
    
'''
import sys
from PyQt5.QtWidgets import QWidget, QToolTip , QApplication
from PyQt5.QtGui import QFont

class exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('这是一个<b>气泡提示</b>')
        self.setGeometry(200, 300, 400, 400)
        self.setWindowTitle('气泡提示demo')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = exp()
    sys.exit(app.exec_())