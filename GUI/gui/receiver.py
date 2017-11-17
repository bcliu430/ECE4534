import socket
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from enum import Enum


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
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, 2000))
        state = STATE.STARTBYTE
        data = []
        count = 0
        numbytes = 0
        while True:
            byte = self.s.recv(1)
            ##            print (state)
            ##            print (byte)
            if byte:
                if (state == STATE.STARTBYTE):
                    if byte == b'\xff':
                        state = STATE.NUMBYTES
                        data.append(byte)
                elif (state == STATE.NUMBYTES):
                    byte = int.from_bytes(byte, byteorder='big')
                    data.append(str(byte))
                    numbytes = byte
                    state = STATE.DATATYPE
                elif (state == STATE.DATATYPE):
                    data.append(byte.decode())
                    state = STATE.DATA
                elif (state == STATE.DATA):
                    byte = int.from_bytes(byte, byteorder='big')
                    data.append(str(byte))
                    count += 1
                    if (count < numbytes):
                        state = STATE.DATATYPE
                    else:
                        data.append(b'\xfe')
                        print('raw data')
                        print(data)
                        count = 0
                        state = STATE.STARTBYTE
                        data = ' '.join(data[1:-1])
                        data = data + '\n'
                        print('receiver: ' + data)
                        self.newdata.emit(data)
                        data = []

    @pyqtSlot(str)
    def sendMsg(self, msg):
        print('send')
        if msg == 'N':
            for b in MSG.North:
                self.s.send(b)
        elif msg == 'S':
            for b in MSG.South:
                self.s.send(b)

        if msg == 'W':
            for b in MSG.West:
                self.s.send(b)

        if msg == 'E':
            for b in MSG.East:
                self.s.send(b)


'''
TODO: 1. emit a signal to send the debug data to GUI
      2. Two state for Controller: 1 moving to a joint, 2 arrive a joint
      3. find when to send the data back    
'''
