#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import * #QApplication, QWidget, QLabel
from PyQt5.QtGui import *
from send import *
from receive import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('Tron Light Bike')
    layout = QHBoxLayout(w)
    send = Send()
    rev  = Receive()
    layout.addWidget(send)
    layout.addWidget(rev)
    w.resize(480, 160)
    w.show() 
    sys.exit(app.exec_())
