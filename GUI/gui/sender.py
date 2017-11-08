import socket
from PyQt5.QtCore import QObject, pyqtSlot

class Sender(QObject):
    @pyqtSlot()
    def sendMsg(msg, host, s):
        print ("message: {}".format(msg))
        for b in msg:
            s.send(b.encode())

