import socket
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, Qt
from enum import Enum
import time


class MSG(Enum):
    North = [b'\xff', b'\x01', b'\x57', b'\x4e', b'\xfe']
    South = [b'\xff', b'\x01', b'\x57', b'\x53', b'\xfe']
    West = [b'\xff', b'\x01', b'\x57', b'\x57', b'\xfe']
    East = [b'\xff', b'\x01', b'\x57', b'\x45', b'\xfe']


class STATE(Enum):
    STARTBYTE = 0
    NUMBYTES = 1
    DATATYPE = 2
    DATA = 3


class Receiver(QObject):
    newdata = pyqtSignal(str)

    @pyqtSlot(str)
    def recvMsg(self, host):
        print( host)
        while True:
#            print('ok')
            data = '1 P f'
            self.newdata.emit(data)
            time.sleep(1)


'''
TODO: 1. emit a signal to send the debug data to GUI
      2. Two state for Controller: 1 moving to a joint, 2 arrive a joint
      3. find when to send the data back    
'''
