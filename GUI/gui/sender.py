import socket
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

up = b'\xff\x01\x57\x4e\xfe' 

class Sender(QObject):

    done = pyqtSignal()

    @pyqtSlot(str, str)
    def sendMsg(self, msg, host):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, 2000))
        print(up)
        for b in msg:
            s.send(b.encode())
        s.close()
