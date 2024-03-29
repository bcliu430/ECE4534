import socket
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QTimer
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
    peter_wait = 0

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
        state = STATE.STARTBYTE
        data = []
        count = 0
        numbytes = 0
        while True:
            byte = self.s.recv(1)
            if byte:
                if (byte == b'\xff'):
                        byte = self.s.recv(1)
                        data.append(byte.decode())
                        byte = self.s.recv(1)
                        data.append(str(byte))
                        byte = self.s.recv(1)
                          
#                        print('raw data')
#                        print(data)
                        data = ' '.join(data)
                        self.newdata.emit(data)
                        if not 'R' in data:
                            if self.peter_flag:
                                self.peter_count += 1
                                if self.peter_count > 10:
                                    print('resend', self.port, self.peter_msg)
                                    self.sendMsg(self.peter_msg)
                                    self.peter_count = 0
                        else:
                            print(self.port, 'received')
                            self.peter_count = 0
                            self.peter_flag = False

                        if not (self.msg == ''): 
                            self.sendMsg(self.msg)
                            self.msg = ''
                        data = []

    def sendMsg(self, msg):
        if (self.port == 2000):
            print( 'user: ======send=====' + msg)
        if (self.port == 3000):
            print( 'ai: ======send=====' + msg)

        if msg == 'left':
            Left = [b'\xff', b'W', b'L', b'\xfe']
            for b in Left:
                self.s.send(b)
        elif msg == 'straight':
            Str = [b'\xff', b'W', b'U', b'\xfe']
            for b in Str:
                self.s.send(b)

        elif msg == 'right':
            Right = [b'\xff', b'W', b'R', b'\xfe']
            for b in Right:
                self.s.send(b)


'''
TODO: 1. emit a signal to send the debug data to GUI
      2. Two state for Controller: 1 moving to a joint, 2 arrive a joint
      3. find when to send the data back    
'''
