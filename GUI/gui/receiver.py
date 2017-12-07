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
    soc = ''
    s = ''
    peter_flag = False
    peter_count = 0
    peter_msg = ''
    def __init__(self, port):
        super(Receiver,self).__init__()
        self.port = port
        self.connect();

    def connect(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.bind(('',self.port))
        self.soc.listen()
        self.s, addr = self.soc.accept()

    @pyqtSlot()
    def recvMsg(self):
#        self.s.connect((self.host, 2000))
        state = STATE.STARTBYTE
        data = []
        count = 0
        numbytes = 0
        while True:
            try:
                self.s.send(b'\x00')
            except:
                self.connect()
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
#                        if ("b'P'" in data):
#                            print ('intersect')
                        if self.peter_flag and not "b'R'" in data:
                            self.peter_count += 1
                            if self.peter_count > 10:
                                self.sendMsg(self.peter_msg)
                                self.peter_count = 0
                        else:
                            self.peter_flag = False

                        if not (self.msg == '') : 
                            print(self.msg)
                            self.sendMsg(self.msg)
                            self.peter_flag = True
                            self.peter_msg = self.msg
                            self.msg = ''
 
                        data = []

    def sendMsg(self, msg):
        if (self.port == 2000):
            print( 'user: ======send=====' + msg)
        if (self.port == 3000):
            print( 'ai: ======send=====' + msg)

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
