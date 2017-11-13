from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Arena(QWidget):
    def __init__(self):
        super(Arena,self).__init__()

        self.hbox = QHBoxLayout()

        self.scene = QGraphicsScene()
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.hbox.addWidget(self.view)
        self.setLayout(self.hbox)

    def draw(self, item):
        self.scene.addItem(item);

    @pyqtSlot(str, str)
    def update_grid(self, curr, new):
        curr = curr.split()
        new = new.split()
        print (curr, new)
        line = QGraphicsLineItem(float(curr[0]), float(curr[1]), 
                                float(new[0]), float(new[1]))
        pen = QPen()
        pen.setColor(Qt.red)
        line.setPen(pen)
        self.item = line
        self.draw(self.item)

