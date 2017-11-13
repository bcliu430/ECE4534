import socket
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from enum import Enum
from bitstring import BitArray

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
                if(state == STATE.STARTBYTE):
                    if byte == b'\xff':
                            state = STATE.NUMBYTES
                            data.append(byte)
                elif(state == STATE.NUMBYTES):
                    byte = int.from_bytes(byte, byteorder='big')
                    data.append(str(byte))
                    numbytes = byte
                    state = STATE.DATATYPE
                elif(state == STATE.DATATYPE):
                    data.append(byte.decode())
                    state = STATE.DATA
                elif(state == STATE.DATA):
                    byte = int.from_bytes(byte, byteorder='big')
                    data.append(str(byte))
                    count += 1
                    if (count < numbytes):
                        state = STATE.DATATYPE
                    else:
                        data.append(b'\xfe')
                        print ('raw data')
                        print(data)
                        count =0
                        state = STATE.STARTBYTE
                        data  = ' '.join(data[1:-1])
                        data  = data +'\n' 
                        print ('receiver: '+data)
                        self.newdata.emit(data)
                        data = []

    @pyqtSlot(str)
    def sendMsg(self, msg):
        prototype = 'ff01w{}fe'.format(msg)
        print(prototype)
        print ("message: {}".format(msg))
        for b in msg:
            self.s.send(b.encode())

'''
TODO: 1. emit a signal to send the debug data to GUI
      2. Two state for Controller: 1 moving to a joint, 2 arrive a joint
      3. find when to send the data back    
'''


