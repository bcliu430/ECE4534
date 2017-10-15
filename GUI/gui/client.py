#!/usr/bin/env python3.6
"""
A simple echo client
"""

import socket

host = ''
port = 20002
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
msg = '*hello*ff010S0efe'
for b in msg:
    s.send(b.encode())
s.close()

