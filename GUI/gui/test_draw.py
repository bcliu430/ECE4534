import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from start import *
from time import sleep


class Test(QWidget):
    def __init__(self):
        super(Test, self).__init__()
        vbox = QVBoxLayout()
        self.start_box = QHBoxLayout()
        vbox.addLayout(self.start_box)
        self.setLayout(vbox)
        self.test()

    def test(self):
        self.start_widget = Start()

        self.start_box.addWidget(self.start_widget)
        self.start_widget.update_grid([0.0,10], [ 100,0] )
        sleep(10)

        self.start_widget.update_grid([0.0,100], [ 10,0] )

def run():

    app = QApplication(sys.argv)
    w = Test()
    w.resize(1200, 450)
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
 
