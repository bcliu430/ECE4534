#!/usr/bin/env python3

"""
A simple echo client
"""

import socket
from time import sleep

host = '192.168.0.16'
port = 2000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))
while 1:
    s.send(b'42')
    sleep(1)
