from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Arena(QWidget):
    def __init__(self):
        super(Arena,self).__init__()

        self.hbox = QHBoxLayout()
        # self.setFixedSize(QRect(20, 40, 601, 501))
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 400, 400)
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.hbox.addWidget(self.view)
        self.setLayout(self.hbox)

        line = QGraphicsLineItem(0.0, 0.0, 400.0, 0.0)
        line1 = QGraphicsLineItem(400, 0.0, 400.0, 400)
        line2 = QGraphicsLineItem(400, 400, 0, 400)
        line3 = QGraphicsLineItem(0, 400.0, 0, 0)

        pen = QPen()
        pen.setColor(Qt.lightGray)
        line.setPen(pen)
        line1.setPen(pen)
        line2.setPen(pen)
        line3.setPen(pen)

        self.draw(line)
        self.draw(line1)
        self.draw(line2)
        self.draw(line3)

    def draw(self, item):
        self.scene.addItem(item);

    @pyqtSlot(str, str)
    def update_grid(self, new, curr):
        curr = curr.split()
        new = new.split()
        print(curr, new)

        multipler = 1

        line = QGraphicsLineItem(float(curr[0]*multipler), float(curr[1]*multipler),
                                 float(new[0]*multipler), float(new[1])*multipler)
        pen = QPen()
        pen.setColor(Qt.red)
        line.setPen(pen)
        self.item = line
        self.draw(self.item)

