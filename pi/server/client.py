#!/usr/bin/env python3.6
"""
A simple echo client
"""

import socket

host = '192.168.0.16'

port = 2000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
while 1:
    data = s.recv(size)
    if data:
        s.send(b'What is the meaning of life?')
    s.close()
    print (b'Received:'+ data)
