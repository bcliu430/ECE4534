from receiver import *
from sender import *
from PyQt5.QtCore import *
import sys

class Controller(QObject):
    def user_thread():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '192.168.0.16'
        port = 2000
        s.connect((host,port))
        objThread = Qthread()
        obj = Receiver()
        obj.moveToThread(objThread)
        obj.newdata.connect(append_data)
        objThread.started.connect(obj.recvMsg(host_user, s))
        objThread.start()

if __name__ == "__main__":
        app = QCoreApplication([])

        sys.exit(app.exec_())


