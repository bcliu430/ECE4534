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

        self.left_btn  = QPushButton('<-')
        self.right_btn = QPushButton('->')

        self.coor_box.addWidget(self.u,     1,0)
        self.coor_box.addWidget(self.u_coor,1,1)
        self.coor_box.addWidget(self.u_dire,1,2)
        self.coor_box.addWidget(self.enter1,1,3)
        self.coor_box.addWidget(self.a     ,2,0)
        self.coor_box.addWidget(self.a_coor,2,1)
        self.coor_box.addWidget(self.a_dire,2,2)
        self.coor_box.addWidget(self.enter2,2,3)

        self.dir_box.addWidget(self.left_btn)
        self.dir_box.addWidget(self.right_btn)

        self.vbox.addLayout(self.coor_box)
        self.vbox.addWidget(self.start)
        self.vbox.addLayout(self.dir_box)
        
        self.hbox.addWidget(self.view)
        self.hbox.addLayout(self.vbox)

        
