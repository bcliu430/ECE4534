from receiver import *
##from receiver_fake import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tron import *
from tron import attack_predict
import sys


# from mainwindow import MainWindow

class Controller(QObject):
    start1 = pyqtSignal(str)
    start2 = pyqtSignal(str)
    cmd1 = pyqtSignal(str) ## update user table
    cmd2 = pyqtSignal(str) ## update AI table
    send_user = pyqtSignal(str)
    send_ai   = pyqtSignal(str)
    user_coor_sig = pyqtSignal(str, str)
    ai_coor_sig = pyqtSignal(str, str)
    host1 = '192.168.0.16'
    host2 = '192.168.0.20'
    port = 2000
    count = 0
    data1 = []
    data2 = []
    user_l = []
    ai_l = []
    multipler = 50
    # width = 30
    # height = 20

    user = Rover()
    ai = Rover()

    def __init__(self):
        super(Controller, self).__init__()
        self.recvThread1 = QThread()
        self.recvThread2 = QThread()
        self.recvObj1 = Receiver(self.host1)
        self.recvObj2 = Receiver(self.host2)
        self.user_dire = Direction.right
        self.ai_dire = Direction.down
        self.recvObj1.moveToThread(self.recvThread1)
        self.recvObj2.moveToThread(self.recvThread2)
        self.start1.connect(self.recvObj1.recvMsg)
        self.start2.connect(self.recvObj2.recvMsg)
        self.recvObj1.newdata.connect(self.append_user_data)
        self.recvObj2.newdata.connect(self.append_ai_data)
        self.user.def_init_pos(1, 1)
        self.ai.def_init_pos(1, 2)
        self.user.add_trace(1,1)
        self.ai.add_trace(1,2)
        self.user_prev = Direction.right
        self.ai_prev = Direction.down
#        self.send_user.connect(self.recvObj1.sendMsg)
#        self.send_ai.connect(self.recvObj2.sendMsg)

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
        self.start1.emit(self.host1)
        self.start2.emit(self.host2)
        self.recvObj1.sendMsg('straight')
        self.recvObj2.sendMsg('straight')

    @pyqtSlot()
    def straight(self):
        print ('call test')
        self.recvObj1.sendMsg('straight')
        self.recvObj1.sendMsg('straight')
        self.recvObj1.sendMsg('straight')

    @pyqtSlot(str)
    def append_user_data(self, data):
        print('user: ' + data)
        temp = data.split()
        self.data1.append(data)
        if (len(self.data1) == 10):
            tmp = '\n'.join(self.data1)
            self.data1 = []
            self.cmd1.emit(tmp)
#        print(temp)
        if "b'P'" in temp:
            print('user hit joint')
            old_x = self.user.trace[-1].x * self.multipler
            old_y = self.user.trace[-1].y * self.multipler
            x, y = self.get_new_coordinates(self.user_dire, 0)

            coordinatex, coordinatey = x/self.multipler, y/self.multipler 


from receiver import *
##from receiver_fake import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tron import *
from tron import attack_predict
import sys


# from mainwindow import MainWindow

class Controller(QObject):
    start1 = pyqtSignal(str)
    start2 = pyqtSignal(str)
    cmd1 = pyqtSignal(str) ## update user table
    cmd2 = pyqtSignal(str) ## update AI table
    send_user = pyqtSignal(str)
    send_ai   = pyqtSignal(str)
    user_coor_sig = pyqtSignal(str, str)
    ai_coor_sig = pyqtSignal(str, str)
    host1 = '192.168.0.16'
    host2 = '192.168.0.20'
    port = 2000
    count = 0
    data1 = []
    data2 = []
    user_l = []
    ai_l = []
    multipler = 50
    # width = 30
    # height = 20

    user = Rover()
    ai = Rover()

    def __init__(self):
        super(Controller, self).__init__()
        self.recvThread1 = QThread()
        self.recvThread2 = QThread()
        self.recvObj1 = Receiver(self.host1)
        self.recvObj2 = Receiver(self.host2)
        self.user_dire = Direction.right
        self.ai_dire = Direction.down
        self.recvObj1.moveToThread(self.recvThread1)
        self.recvObj2.moveToThread(self.recvThread2)
        self.start1.connect(self.recvObj1.recvMsg)
        self.start2.connect(self.recvObj2.recvMsg)
        self.recvObj1.newdata.connect(self.append_user_data)
        self.recvObj2.newdata.connect(self.append_ai_data)
        self.user.def_init_pos(1, 1)
        self.ai.def_init_pos(1, 2)
        self.user.add_trace(1,1)
        self.ai.add_trace(1,2)
        self.user_prev = Direction.right
        self.ai_prev = Direction.down
#        self.send_user.connect(self.recvObj1.sendMsg)
#        self.send_ai.connect(self.recvObj2.sendMsg)

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
        self.start1.emit(self.host1)
        self.start2.emit(self.host2)
        self.recvObj1.sendMsg('straight')
        self.recvObj2.sendMsg('straight')
        if direct == Direction.down:
            return 'down'
        if direct == Direction.left:
            return 'left'
        if direct == Direction.right:
            return 'right'

    def get_rover_direction(self, data):
        print (data)
        first = data[0]
        second = data[1]
        third = data[2]
        if (first[0] == second[0] == third[0]) or (first[1] == second[1] == third[1]):
            return "straight"
        else:
            if (first[0] == second[0] and second[1] == third[1]): ## y direction
                if(second[1] - first[1] < 0):
                    if(third[0] - second[0] >0):
                        return "right"
                    else:
                        
                        return "left"
                else:
                    if(third[0] - second[0] >0):
                        return "left"
                    else:
                        return "right"
 
            if (first[1] == second[1] and second[0] == third[0]): ## x direction 
                if(second[0] - first[0] < 0):
                    if(third[1] - second[1] >0):
                        return "left"
                    else:
                        return "right"
                else:
                    if(third[1] - second[1] >0):
                        return "right"
                    else:
                        return "left"

    def get_rover_dir(self, prev, new):
        prev = self.get_direction_rev(prev)
        new = self.get_direction_rev(new)
        if prev == 'up':
            if new == 'up' or new == 'down':
                return 'straight'
            else: 
                return new
        elif prev == 'down': 
            if new == 'up' or new == 'down':
                return 'straight'
            elif new  == 'left':
                return 'right'
            elif new == 'right':
                return 'left'
        elif prev == 'left':
            if new == 'left' or new == 'right':
                return 'straight'
            elif new == 'up':
                return 'right'
            elif new == 'down':
                return 'left'

        elif prev == 'right':
            if new == 'left' or new == 'right':
                return 'straight'
            elif new == 'up':
                return 'left'
            elif new == 'down':
                return 'right'

               
'''
if __name__ == "__main__":
    app = QCoreApplication([])
    msg = 'hello'
    c = Controller()
    c.start()
    print('test')
    sys.exit(app.exec_())
'''
