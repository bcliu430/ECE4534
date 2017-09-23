#!/usr/bin/env python

"""
A simple echo server
"""

import socket

host = '192.168.0.16'
port = 2000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    print (b'Received : ' + data)
    if data:
        client.send(data)
    client.close()
