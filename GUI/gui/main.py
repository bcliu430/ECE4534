#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from mainwindow import *

def run():

    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(900, 400)
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
