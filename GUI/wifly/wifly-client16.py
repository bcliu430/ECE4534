#!/usr/bin/env python3

import serial
from time import sleep


dev='/dev/ttyUSB1'
baud=57600
ssid='Team16_pi'
s = serial.Serial(dev, baud, timeout=1)

def send_cmd(s, cmd):
    for c in cmd:
        s.write(c)
        sleep(0.1)

def get_reply(s):
    reply = s.readlines()
    return reply

def test_conn():

    send_cmd(s, '$$$')
    reply = get_reply(s)
    if 'CMD' in reply:
        send_cmd(s, 'join '+ssid)
        reply = get_reply(s)
        if '...' in reply:
            return true

def main():
    while 1:
        if b'*OPEN*' in get_reply(s):
            break
    print ('debug')
    while 1:
        print(get_reply(s))
        msg = [b'\xff', b'\x01', b'\x4c', b'\x00', b'\xfe']
        send_cmd(s, msg)
        sleep(3)

        msg = [b'\xff', b'\x02', b'\x4c', b'\x00', b'\x53', b'\x05', b'\xfe']
        send_cmd(s, msg)
        sleep(3)

        msg = [b'\xff', b'\x01', b'\x50', b'\x0f', b'\xfe']
        send_cmd(s, msg)
        sleep(3)



main() 
