from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Arena import Arena
from tron import Direction
from Controller import Controller

class start(QWidget):
    user_loc = pyqtSignal(str)
    ai_loc = pyqtSignal(str)
    direction = pyqtSignal(Direction)
    start = pyqtSignal()
    def __init__(self, controller):
        super(start,self).__init__()
        self.coor_box = QGridLayout()
        self.dir_box =  QGridLayout()

        self.view = Arena()
        self.c = controller
        self.user_loc.connect(self.c.user_loc_init)
        self.ai_loc.connect(self.c.ai_loc_init)
        self.direction.connect(self.c.user_dir)
        self.c.user_coor_sig.connect(self.view.update_grid)
        self.c.ai_coor_sig.connect(self.view.update_ai_grid)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.view)
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
        self.bottom_btn  = QToolButton()
        self.right_btn  = QToolButton()

        self.left_btn.setArrowType(Qt.LeftArrow)
        self.up_btn.setArrowType(Qt.UpArrow)
        self.bottom_btn.setArrowType(Qt.DownArrow)
        self.right_btn.setArrowType(Qt.RightArrow)
        self.left_btn.setIconSize(QSize(100, 100))
        self.up_btn.setIconSize(QSize(100, 100))
        self.bottom_btn.setIconSize(QSize(100, 100))
        self.right_btn.setIconSize(QSize(100, 100))

        self.coor_box.addWidget(self.u,     1,0)
        self.coor_box.addWidget(self.u_coor,1,1)
        self.coor_box.addWidget(self.u_dire,1,2)
        self.coor_box.addWidget(self.enter1,1,3)
        self.coor_box.addWidget(self.a     ,2,0)
        self.coor_box.addWidget(self.a_coor,2,1)
        self.coor_box.addWidget(self.a_dire,2,2)
        self.coor_box.addWidget(self.enter2,2,3)

        self.dir_box.addWidget(self.left_btn, 1, 0)
        self.dir_box.addWidget(self.up_btn, 0, 1)
        self.dir_box.addWidget(self.bottom_btn, 1, 1)
        self.dir_box.addWidget(self.right_btn, 1,2)

        self.vbox.addLayout(self.coor_box)
        self.vbox.addWidget(self.start)
        self.vbox.addLayout(self.dir_box)
        
        self.hbox.addLayout(self.vbox)

        self.start.clicked.connect(self.start_slot)
        self.enter1.clicked.connect(self.enter1_text)
        self.enter2.clicked.connect(self.enter2_text)

        self.left_btn.clicked.connect(self.on_left)
        self.up_btn.clicked.connect(self.on_up)
        self.bottom_btn.clicked.connect(self.on_bottom)
        self.right_btn.clicked.connect(self.on_right)

    @pyqtSlot()
    def start_slot(self):
        print("start pressed")
        self.c.start()

    @pyqtSlot()
    def enter1_text(self):
        co = self.u_coor.text()
        d = self.u_dire.text()
        self.user_loc.emit(co+' '+d)

    @pyqtSlot()
    def enter2_text(self):
        co = self.a_coor.text()
        d = self.a_dire.text()
        self.ai_loc.emit(co+' '+d)
        # print (co, d)

    @pyqtSlot()
    def on_left(self):
        # print('W')
        self.direction.emit(Direction.left)

    @pyqtSlot()
    def on_up(self):
        # print('N')
        self.direction.emit(Direction.up)
        
    @pyqtSlot()
    def on_bottom(self):
        # print('S')
        self.direction.emit(Direction.down)

    @pyqtSlot()
    def on_right(self):
        # print('E')
        self.direction.emit(Direction.right)
