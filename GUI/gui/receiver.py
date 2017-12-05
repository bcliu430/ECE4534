import socket
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from enum import Enum

class STATE(Enum):
    STARTBYTE = 0
    NUMBYTES = 1
    DATATYPE = 2
    DATA = 3


class Receiver(QObject):
    newdata = pyqtSignal(str)
    msg = ''
    def __init__(self, host):
        super(Receiver,self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.s.connect((host, 2000))

    @pyqtSlot(str)
    def recvMsg(self):
#        self.s.connect((self.host, 2000))
        state = STATE.STARTBYTE
        data = []
        count = 0
        numbytes = 0
        while True:
            self.s.send(b'\x00')
            byte = self.s.recv(1)
            ##            print (state)
        ##           print (byte)
            if byte:
                if (state == STATE.STARTBYTE or byte == b'\xff'):
                        state = STATE.NUMBYTES
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
#                        print('raw data')
#                        print(data)
                        count = 0
                        state = STATE.STARTBYTE
                        data = ' '.join(data)
                        data = data + '\n'
                        self.newdata.emit(data)
                        if ("b'P'" in data):
                            print ('intersect')
                            while self.msg == '':
                                pass
                            print(self.msg)
                            self.sendMsg(self.msg)
                            self.sendMsg(self.msg)
                            self.sendMsg(self.msg)
                            self.msg = ''
 
                        data = []

    def sendMsg(self, msg):
        print( '======send=====' + msg)
        if msg == 'left':
            Left = [b'\xff', b'\x01', b'W', b'L', b'\xfe']
            for b in Left:
                print (b)
                self.s.send(b)
        elif msg == 'straight':
            Str = [b'\xff', b'\x01', b'\x57', b'\x55', b'\xfe']
            for b in Str:
                self.s.send(b)

        if msg == 'right':
            Right = [b'\xff', b'\x01', b'\x57', b'\x52', b'\xfe']
            for b in Right:
                self.s.send(b)


'''
TODO: 1. emit a signal to send the debug data to GUI
      2. Two state for Controller: 1 moving to a joint, 2 arrive a joint
      3. find when to send the data back    
'''
