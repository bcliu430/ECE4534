# from receiver import *
from receiver_fake import *
from getCoor import Coor
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tron import *
import sys


# from mainwindow import MainWindow

class Controller(QObject):
    coor = Coor()
    appStart = pyqtSignal(str)
    cmd1 = pyqtSignal(str)
    user_coor_sig = pyqtSignal(str, str)

    host = '192.168.0.16'
    port = 2000
    count = 0
    data_l = []

    width = 30
    height = 20

    user = Rover()
    ai = Rover()

    def __init__(self):
        super(Controller, self).__init__()
        self.recvThread1 = QThread()
        self.recvObj1 = Receiver()
        self.user_dire = Direction.up
        self.recvObj1.moveToThread(self.recvThread1)
        self.appStart.connect(self.recvObj1.recvMsg)
        self.recvObj1.newdata.connect(self.append_user_data)

    def get_new_user_coordinates(self, direction):
        x = self.user.trace[-1].x
        y = self.user.trace[-1].y
        if direction == Direction.up:
            y = y - 1
        elif direction == Direction.down:
            y = y + 1
        elif direction == Direction.left:
            x = x - 1
        elif direction == Direction.right:
            x = x + 1
        return x, y

    @pyqtSlot()
    def start(self):
        print("start")
        self.recvThread1.start()
        self.appStart.emit(self.host)

    @pyqtSlot(str)
    def append_user_data(self, data):
        print(data)
        self.count += 1
        temp = data.split()

        if 'P' in temp:
            print('hit joint')
            #               get user input/ AI next coordinate here
            #               get this part working
            # new_coor = self.coor.getNewCoor(self.user_coor, self.user_dire)
            # self.user_coor_list.append(new_coor)
            # self.user_coor_sig.emit(str(new_coor[0]) + ' ' + str(new_coor[1]), '0 0')  ## not work
            old_x = self.user.trace[-1].x
            old_y = self.user.trace[-1].y
            # print()
            # print('old_x, old_y' , old_x, old_y)
            x, y = self.get_new_user_coordinates(self.user_dire)
            self.user.add_trace(x, y)
            self.user_coor_sig.emit(str(x) + ' ' + str(y), str(old_x) + ' ' + str(old_y))
            # print(self.user.trace)
            #        print('Controller: '+data)

    @pyqtSlot(str)
    def user_loc(self, msg):
        print(msg)
        msg = msg.split()
        self.user_dire = self.get_direction(msg[2])
        self.user.add_trace(int(msg[0]), int(msg[1]))
        self.user.def_init_pos(int(msg[0]), int(msg[1]))
        ## emit a direction to wifly

    @pyqtSlot(Direction)
    def user_dir(self, direction):
        self.user_dire = direction
        print("in ctler:", self.user_dire)

    def get_direction(self, direct):
        if direct == "up":
            return Direction.up
        if direct == "down":
            return Direction.down
        if direct == "left":
            return Direction.left
        if direct == "right":
            return Direction.right


if __name__ == "__main__":
    app = QCoreApplication([])
    msg = 'hello'
    c = Controller()
    c.start()
    print('test')
    sys.exit(app.exec_())
