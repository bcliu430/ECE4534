import socket
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class Sender(QObject):

    done = pyqtSignal()

    @pyqtSlot(str, str)
    def sendMsg(self, msg, host):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, 2000))
        prototype = 'ff01w{}fe'.format(msg)
        print(prototype)
        print ("message: {}".format(msg))
        for b in msg:
            s.send(b.encode())
        s.close()
