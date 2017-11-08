import socket
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

class Receiver(QObject):

    newdata = pyqtSignal()

    @pyqtSlot()
    def recvMsg(self, host, s):
        while True:
            data = ''
            byte = s.recv(1).decode()
            if byte == '0xff':
                data = byte
                while True:
                    byte = s.recv(1).decode()
                    data +=byte
                    if byte == '0xfe':
                        break
                data = parse(data)
                self.newdata.emit(data) 

    def parse(self, data):
        return ([data[i:i+2] for i in range(0, len(data))])

