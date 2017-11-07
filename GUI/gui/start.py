from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Start(QWidget):
    def __init__(self):
        super(Start,self).__init__()
        self.coor_box = QGridLayout()
        self.dir_box =  QHBoxLayout()
        
        self.scene = QGraphicsScene()
        self.view = QGraphicsView()
        self.view.setScene(self.scene)

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.setLayout(self.hbox)
        self.main()

    def main(self):
        self.u    = QLabel('user')
        self.a    = QLabel('AI')
        self.u_coor = QLineEdit()
        self.u_coor.setPlaceholderText('Coordinate')
        self.a_coor = QLineEdit()
        self.a_coor.setPlaceholderText('Coordinate')
        self.u_dire = QLineEdit()
        self.u_dire.setPlaceholderText('Direction')
        self.a_dire = QLineEdit()
        self.a_dire.setPlaceholderText('Direction')
        self.enter1 = QPushButton('Enter')
        self.enter2 = QPushButton('Enter')

        self.start = QPushButton("Start") #first box
        self.start.setMaximumWidth(300)
        self.start.setMinimumHeight(50)
        
        self.left_btn  = QToolButton()
        self.up_btn  = QToolButton()
        self.right_btn  = QToolButton()
        self.left_btn.setArrowType(Qt.LeftArrow)
        self.up_btn.setArrowType(Qt.UpArrow)
        self.right_btn.setArrowType(Qt.RightArrow)
        self.left_btn.setIconSize(QSize(100, 100))
        self.up_btn.setIconSize(QSize(100, 100))
        self.right_btn.setIconSize(QSize(100, 100))

        self.coor_box.addWidget(self.u,     1,0)
        self.coor_box.addWidget(self.u_coor,1,1)
        self.coor_box.addWidget(self.u_dire,1,2)
        self.coor_box.addWidget(self.enter1,1,3)
        self.coor_box.addWidget(self.a     ,2,0)
        self.coor_box.addWidget(self.a_coor,2,1)
        self.coor_box.addWidget(self.a_dire,2,2)
        self.coor_box.addWidget(self.enter2,2,3)

        self.dir_box.addWidget(self.left_btn)
        self.dir_box.addWidget(self.up_btn)
        self.dir_box.addWidget(self.right_btn)

        self.vbox.addLayout(self.coor_box)
        self.vbox.addWidget(self.start)
        self.vbox.addLayout(self.dir_box)
        
        self.hbox.addWidget(self.view)
        self.hbox.addLayout(self.vbox)

    def draw(self, item):
        self.scene.addItem(item);

    def update_grid(self, curr, new):
        line = QGraphicsLineItem(curr[0], curr[1], new[0], new[1])
        pen = QPen()
        pen.setColor(Qt.red)
        line.setPen(pen)
        self.item = line
        self.draw(self.item)
