##from receiver import *
from receiver_fake import *
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
    multipler = 20
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
        self.start1.connect(self.recvObj1.recvMsg)
        self.start2.connect(self.recvObj2.recvMsg)
        self.recvObj1.newdata.connect(self.append_user_data)
        self.recvObj2.newdata.connect(self.append_ai_data)
        self.send_user.connect(self.recvObj1.sendMsg)
        self.send_ai.connect(self.recvObj2.sendMsg)

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

    @pyqtSlot(str)
    def append_user_data(self, data):
#        print(data)
        self.count += 1
        temp = data.split()
        self.data1.append(data)
        if (len(self.data1) == 10):
            tmp = '\n'.join(self.data1)
            self.data1 = []
            self.cmd1.emit(tmp)
        if 'P' in temp:
#            print('user hit joint')
            ##print (self.user.trace[-1].x, self.user.trace[-1].y)
            old_x = self.user.trace[-1].x * self.multipler
            old_y = self.user.trace[-1].y * self.multipler
            x, y = self.get_new_coordinates(self.user_dire, 0)
            self.send_user.emit('left') ## not work?
            coordinatex, coordinatey = x/self.multipler, y/self.multipler 

            if ([coordinatex, coordinatey] in self.user_l[:-1]) or ([coordinatex, coordinatey] in self.ai_l)  or x < 0 or y < 0 or coordinatex > 16 or coordinatey >10:
                if [coordinatex, coordinatey] == self.user_l[-1]:
                    print ('both lose')
                else:
                    print ('ai win')
                self.recvThread1.terminate()
                self.recvThread2.terminate()
            else:
                self.user_l.append([x/self.multipler, y/self.multipler])
                if (len(self.user_l) > 2):
                    rover_direction = self.get_rover_direction(self.user_l[-3:])
                    print(rover_direction)
                self.user.add_trace(int(x/self.multipler), int(y/self.multipler))
                self.user_coor_sig.emit(str(x) + ' ' + str(y), str(old_x) + ' ' + str(old_y))

    @pyqtSlot(str)
    def append_ai_data(self, data):
        # self.count += 1
        temp = data.split()
        self.data2.append(data)
        if (len(self.data2) == 10):
            tmp = '\n'.join(self.data2)
            self.data2 = []
            self.cmd2.emit(tmp)
        if 'P' in temp:
#            print('ai hit joint')
            old_x = self.ai.trace[-1].x * self.multipler
            old_y = self.ai.trace[-1].y * self.multipler
            x, y = self.get_new_coordinates(self.ai_dire, 1)
            self.send_ai.emit('right')
            coordinatex, coordinatey = x/self.multipler, y/self.multipler 

            if ([coordinatex, coordinatey] in self.user_l) or ([coordinatex, coordinatey] in self.ai_l[:-1])  or x < 0 or y < 0 or coordinatex > 16 or coordinatey >10:
                if [coordinatex, coordinatey] == self.user_l[-1]:
                    print ('both lose')
                else:
                    print ('user win')
                self.recvThread1.terminate()
                self.recvThread2.terminate()
            else:
                self.ai_l.append([coordinatex, coordinatey])
                self.ai.add_trace(int(coordinatex), int(coordinatey))
                self.ai_coor_sig.emit(str(x) + ' ' + str(y), str(old_x) + ' ' + str(old_y))
                self.ai_dire = attack_predict(self.ai, self.user)
                map, hit = visualize_map(self.user.trace, self.ai.trace)
##            print(map)

    @pyqtSlot(str)
    def user_loc_init(self, msg):
        print(msg)
        msg = msg.split()
        self.user_dire = self.get_direction(msg[2])
        self.user_l.append([int(msg[0]), int(msg[1])])
        self.user.add_trace(int(msg[0]), int(msg[1]))
        self.user.def_init_pos(int(msg[0]), int(msg[1]))

    @pyqtSlot(str)
    def ai_loc_init(self, msg):
        print(msg)
        msg = msg.split()
        self.ai_dire = self.get_direction(msg[2])
        # initialize ai starting direction
        self.ai_l.append([int(msg[0]), int(msg[1])])
        self.ai.add_trace(int(msg[0]), int(msg[1]))
        self.ai.def_init_pos(int(msg[0]), int(msg[1]))

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
                
'''
if __name__ == "__main__":
    app = QCoreApplication([])
    msg = 'hello'
    c = Controller()
    c.start()
    print('test')
    sys.exit(app.exec_())
'''
