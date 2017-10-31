#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import * #QApplication, QWidget, QLabel
from PyQt5.QtGui import *

class Receive(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.init()

    def init(self):        
        label = QLabel('Receive: ');
        line = QLineEdit();
        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(line)
         
