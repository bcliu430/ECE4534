#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import * #QApplication, QWidget, QLabel
from PyQt5.QtGui import *
def send():
    w = QWidget()
    l = QHBoxLayout(w)
    b = QLabel('send: ')
    LE = QLineEdit() 
    return b
    

def receive():
    b = QLabel('receive: ')
    return b

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('Tron Light Bike')
    layout = QHBoxLayout(w)
    send = send()
    rev = receive()
    LE1 = QLineEdit()
    LE2 = QLineEdit()
    layout.addWidget(send)
    layout.addWidget(LE1)
    layout.addWidget(rev)
    layout.addWidget(LE2)
    w.resize(480, 160)
    w.show() 
    sys.exit(app.exec_())
