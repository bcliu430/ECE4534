from receiver import *
from sender import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from time import sleep
class Controller(QObject):
    appStart = pyqtSignal(str)
    cmd = pyqtSignal(str,str)
    host = '192.168.0.16'
    port = 2000
    count = 0
    data_l = []
    def __init__(self):
        super(Controller, self).__init__()

        self.recvThread = QThread()
        self.recvObj = Receiver()
        self.recvObj.moveToThread(self.recvThread)
        self.appStart.connect(self.recvObj.recvMsg)

        self.sendThread = QThread()
        self.sendObj = Sender()
        self.sendObj.moveToThread(self.sendThread)
        self.cmd.connect(self.sendObj.sendMsg)

        self.recvObj.newdata.connect(self.append_data)
    def start(self):
        self.recvThread.start()
        self.sendThread.start()
        self.appStart.emit(self.host)
#        self.cmd.emit(('hello'), self.host)
#        sleep(3)
#        self.cmd.emit(('hello'), self.host)
    @pyqtSlot(str)
    def append_data(self, data):
        self.count +=1
        self.data_l.append(data)
        temp = data.split()
        for i in range(0, int(temp[0])):
            if 'p' in temp and 'f' in temp:
                print('hit joint')
            else:
                pass
        print('Controller'+data)
    


if __name__ == "__main__":
        app = QCoreApplication([])
        msg = 'hello'
        c = Controller()
        c.start()
        print('test')
        sys.exit(app.exec_())


