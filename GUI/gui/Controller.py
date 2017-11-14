from receiver import *
from sender import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
#from mainwindow import MainWindow

class Controller(QObject):
    appStart = pyqtSignal(str)
    cmd1 = pyqtSignal(str)
    user_update_table = pyqtSignal(list)
    host = '192.168.0.16'
    port = 2000
    count = 0
    data_l = []
#    m = MainWindow()
    def __init__(self):
        super(Controller, self).__init__()

        self.recvThread1 = QThread()
        self.recvObj1 = Receiver()
        self.recvObj1.moveToThread(self.recvThread1)
        self.appStart.connect(self.recvObj1.recvMsg)
        self.GUI_thread = QThread()
 #       self.sendThread  QThread()
 #       self.sendObj = Sender()
 #       self.sendObj.moveToThread(self.sendThread)
        self.cmd1.connect(self.recvObj1.sendMsg) ## not connected???
        self.recvObj1.newdata.connect(self.append_data)
 #       self.user_update_table.connect(m.update_user)

    def start(self):
        self.recvThread1.start()
        self.appStart.emit(self.host)

    @pyqtSlot(str)
    def append_data(self, data):
        self.count +=1
        self.data_l.append(data)
        temp = data.split()


        for i in range(0, int(temp[0])):
            if 'P' in temp:
                print('hit joint')       
#               get user input/ AI next coordinate here
#                self.stop.emit()
#               get this part working
                self.cmd1.emit('1')
            else:
                pass
#        if (len(data_l) == 10):
#            self.user_update_table.emit(data_l)
#        print('Controller: '+data)
    
if __name__ == "__main__":
    app = QCoreApplication([])
    msg = 'hello'
    c = Controller()
    c.start()
    print('test')
    sys.exit(app.exec_())
