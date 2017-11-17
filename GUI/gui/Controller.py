# from receiver import *
from receiver_fake import *
from getCoor import Coor
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tron import *
from tron import attack_predict
import sys


# from mainwindow import MainWindow

class Controller(QObject):
    coor = Coor()
    appStart = pyqtSignal(str)
    cmd1 = pyqtSignal(str)
    user_coor_sig = pyqtSignal(str, str)
    ai_coor_sig = pyqtSignal(str, str)
    host = '192.168.0.16'
    port = 2000
    count = 0
    data_l = []
    multipler = 10
    # width = 30
    # height = 20

    user = Rover()
    ai = Rover()

    def __init__(self):
        super(Controller, self).__init__()
        self.recvThread1 = QThread()
        self.recvThread2 = QThread()
        self.recvObj1 = Receiver()
        self.recvObj2 = Receiver()
        self.user_dire = Direction.up
        self.ai_dire = Direction.up
        self.recvObj1.moveToThread(self.recvThread1)
        self.recvObj2.moveToThread(self.recvThread2)
        self.appStart.connect(self.recvObj1.recvMsg)
        self.appStart.connect(self.recvObj2.recvMsg)
        self.recvObj1.newdata.connect(self.append_user_data)
        self.recvObj2.newdata.connect(self.append_ai_data)

    # user 0 ai 1
    def get_new_coordinates(self, direction, user_or_ai):
        if user_or_ai == 0:
            x = self.user.trace[-1].x
            y = self.user.trace[-1].y
        else:
            x = self.ai.trace[-1].x
            y = self.ai.trace[-1].y

        x = x * self.multipler
        y = y * self.multipler

        if direction == Direction.up:
            y = y - self.multipler
        elif direction == Direction.down:
            y = y + self.multipler
        elif direction == Direction.left:
            x = x - self.multipler
        elif direction == Direction.right:
            x = x + self.multipler
        return x, y

    @pyqtSlot()
    def start(self):
        print("start")
        self.recvThread1.start()
        self.recvThread2.start()
        self.appStart.emit(self.host)

    @pyqtSlot(str)
    def append_user_data(self, data):
        print(data)
        self.count += 1
        temp = data.split()

        if 'P' in temp:
            print('user hit joint')
            old_x = self.user.trace[-1].x * self.multipler
            old_y = self.user.trace[-1].y * self.multipler
            x, y = self.get_new_coordinates(self.user_dire, 0)
            self.user.add_trace(int(x/self.multipler), int(y/self.multipler))
            self.user_coor_sig.emit(str(x) + ' ' + str(y), str(old_x) + ' ' + str(old_y))

    @pyqtSlot(str)
    def append_ai_data(self, data):
        print(data)
        # self.count += 1
        temp = data.split()

        if 'P' in temp:
            print('ai hit joint')
            old_x = self.ai.trace[-1].x * self.multipler
            old_y = self.ai.trace[-1].y * self.multipler
            x, y = self.get_new_coordinates(self.ai_dire, 1)

            self.ai.add_trace(int(x/self.multipler), int(y/self.multipler))
            self.ai_coor_sig.emit(str(x) + ' ' + str(y), str(old_x) + ' ' + str(old_y))
            self.ai_dire = attack_predict(self.ai, self.user)
            map, hit = visualize_map(self.user.trace, self.ai.trace)
            print(map)

    @pyqtSlot(str)
    def user_loc_init(self, msg):
        print(msg)
        msg = msg.split()
        self.user_dire = self.get_direction(msg[2])
        self.user.add_trace(int(msg[0]), int(msg[1]))
        self.user.def_init_pos(int(msg[0]), int(msg[1]))
        ## emit a direction to wifly

    @pyqtSlot(str)
    def ai_loc_init(self, msg):
        print(msg)
        msg = msg.split()
        self.ai_dire = self.get_direction(msg[2])
        x = int(msg[0])
        y = int(msg[1])
        # initialize ai starting direction
        self.ai.add_trace(x, y)
        self.ai.def_init_pos(x, y)

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
