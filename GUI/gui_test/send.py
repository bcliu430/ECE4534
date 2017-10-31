#!/usr/bin/python3

import sys
import socket
from PyQt5.QtWidgets import * #QApplication, QWidget, QLabel
from PyQt5.QtGui import *

host = '192.168.0.16'
port = 2000
size = 1024
class Send(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.init()

    def init(self):        
        label = QLabel('Send: ');
        line = QLineEdit();

        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(line)
        line.returnPressed.connect(self.sendData)

    def sendData(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        s.send(b'test python')
        print ('enter pressed')
        s.close()
