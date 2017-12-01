import socket
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from enum import Enum


class MSG(Enum):
    Left = [b'\xff', b'\x01', b'\x57', b'\x4c', b'\xfe']
    Str = [b'\xff', b'\x01', b'\x57', b'\x55', b'\xfe']
    Right = [b'\xff', b'\x01', b'\x57', b'\x52', b'\xfe']


class STATE(Enum):
    STARTBYTE = 0
    NUMBYTES = 1
    DATATYPE = 2
    DATA = 3


class Receiver(QObject):
    newdata = pyqtSignal(str)
    def __init__(self, host):
        super(Receiver,self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, 2000))
   
    @pyqtSlot(str)
    def recvMsg(self):
        state = STATE.STARTBYTE
        data = []
        count = 0
        numbytes = 0
        while True:
            byte = self.s.recv(1)
            ##            print (state)
            ##            print (byte)
            if byte:
                if (state == STATE.STARTBYTE or byte == b'\xff'):
                        state = STATE.NUMBYTES
                        data.append(byte)
                elif (state == STATE.NUMBYTES):
                    byte = int.from_bytes(byte, byteorder='big')
                    data.append(str(byte))
                    numbytes = byte
                    state = STATE.DATATYPE
                elif (state == STATE.DATATYPE):
                    data.append(str(byte))
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

        if self.msg != '':
            print( self.msg)
            sendMsg(self.msg)
            self.msg = ''


    def sendMsg(self, msg):
        print( '======send=====')
        if msg == 'left':
            for b in MSG.Left:
                self.s.send(b)
        elif msg == 'straight':
            for b in MSG.Str:
                self.s.send(b)

        if msg == 'right':
            for b in MSG.Right:
                self.s.send(b)


'''
TODO: 1. emit a signal to send the debug data to GUI
      2. Two state for Controller: 1 moving to a joint, 2 arrive a joint
      3. find when to send the data back    
'''
