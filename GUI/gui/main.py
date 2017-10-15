#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from mainwindow import *

def run():

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(1200, 450)
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
