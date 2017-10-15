#!/usr/bin/env python3

import socket
import threading 
from PyQt5 import *

class Server(QtCore.QObject): 
#    def __init__(self):
#        threading.Thread.__init__(self)
    def __init__(self, parent):
        QtCore.QObject.__init__(self, parent)
        self._running = True

        host = ''
        port = 2001
        backlog = 5
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host,port))
        self.s.listen(backlog)

    def run(self):
        print ('in server run' + str(self._running))
        data = ''
        while self._running:
            client, address = self.s.accept()
            byte = client.recv(1).decode()
            if byte == '*':
                data = byte
                byte = client.recv(1).decode()
                while byte != '*':
                    data += byte
                    byte = client.recv(1).decode()
            
                data += byte
                print ('connected to client')
            
            byte = client.recv(2).decode()
            while byte == 'ff':
                data = ''
                byte = client.recv(2).decode()
                while byte != 'fe':
                    data += byte
                    byte = client.recv(2).decode()
            for i in range(len(data)):
                if (data[i] == 'S'):
                    print (data[i+1:i+3])
                    b = int(data[i+1:i+3], 16)
                    print (b) 
            print (data) 
            client.close()
    def stop(self):
        print ("stop signal")
        self._running = False
        self.run()


