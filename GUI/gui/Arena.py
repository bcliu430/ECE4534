from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Arena(QWidget):
    def __init__(self):
        super(Arena,self).__init__()
        self.multipler = 1
        self.hbox = QHBoxLayout()
        # self.setFixedSize(QRect(20, 40, 601, 501))
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(-20, -20, 340, 220)
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.hbox.addWidget(self.view)
        self.setLayout(self.hbox)

        line = QGraphicsLineItem(-20, -20, 340, -20)
        line1 = QGraphicsLineItem(340, -20, 340, 220)
        line2 = QGraphicsLineItem(340, 220, -20, 220)
        line3 = QGraphicsLineItem(-20, 220, -20, -20)

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

        for i in range(0, 300, 50):
            linex = QGraphicsLineItem(i, 0, i, 150)
            linex.setPen(pen)
            self.draw(linex)

        for i in range(0, 200, 50):
            linex = QGraphicsLineItem(0, i, 250, i)
            linex.setPen(pen)
            self.draw(linex)

    def draw(self, item):
        self.scene.addItem(item);

    @pyqtSlot(str, str)
    def update_grid(self, new, curr):
        curr = curr.split()
        new = new.split()
##        print(curr, new)
        multipler = self.multipler

        line = QGraphicsLineItem(float(curr[0]*multipler), float(curr[1]*multipler),
                                 float(new[0]*multipler), float(new[1])*multipler)
        pen = QPen()
        pen.setColor(Qt.red)
        pen.setWidth(5)
        line.setPen(pen)
        self.item = line
        self.draw(self.item)

    @pyqtSlot(str, str)
    def update_ai_grid(self, new, curr):
        curr = curr.split()
        new = new.split()

        multipler = self.multipler
        line = QGraphicsLineItem(float(curr[0] * multipler), float(curr[1] * multipler),
                                 float(new[0] * multipler), float(new[1]) * multipler)
        pen = QPen()
        pen.setColor(Qt.green)
        pen.setWidth(5)
        line.setPen(pen)
        self.item = line
        self.draw(self.item)
