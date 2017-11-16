#from receiver import *
from receiver_fake import *
from getCoor import Coor
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
#from mainwindow import MainWindow

class Controller(QObject):
    coor = Coor()
    appStart = pyqtSignal(str)
    cmd1 = pyqtSignal(str)
    user_coor_sig = pyqtSignal(str)

    host = '192.168.0.16'
    port = 2000
    count = 0
    data_l = []
    user_coor_list = [] 
    user_coor = [1, 2]
    user_dire = 'N'
    def __init__(self):
        super(Controller, self).__init__()
        self.recvThread1 = QThread()
        self.recvObj1 = Receiver()
        self.recvObj1.moveToThread(self.recvThread1)
        self.appStart.connect(self.recvObj1.recvMsg)
        self.recvObj1.newdata.connect(self.append_data)

    @pyqtSlot()
    def start(self):
        print ("start")
        self.recvThread1.start()
        self.appStart.emit(self.host)

    @pyqtSlot(str)
    def append_data(self, data):
        print (data)
        self.count +=1
        temp = data.split()

        if 'P' in temp:
            print('hit joint')       
#               get user input/ AI next coordinate here
#               get this part working
            new_coor = self.coor.getNewCoor(self.user_coor, self.user_dire) 
            self.user_coor_list.append(new_coor)
            self.user_coor_sig.emit(str(new_coor[0]) + ' '+ str(new_coor[1])) ## not work
            print(self.user_coor_list) 
#        print('Controller: '+data)

    @pyqtSlot(str)
    def user_loc(self, msg):
        print (msg)
        msg = msg.split()
        self.user_coor = [msg[0], msg[1]]
        self.user_dire = msg[2]
        self.user_coor_list.append(self.user_coor)
        ## emit a direction to wifly

    @pyqtSlot(str)
    def user_dir(self, direction):
        self.user_dire = direction
        print ("in ctler:"+ self.user_dire)

if __name__ == "__main__":
    app = QCoreApplication([])
    msg = 'hello'
    c = Controller()
    c.start()
    print('test')
    sys.exit(app.exec_())
