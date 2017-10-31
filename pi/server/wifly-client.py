#!/usr/bin/env python3

import serial
import time.sleep

dev='/dev/...'
baud=57600
ssid=


def send_cmd(s, cmd):
    for c in cmd:
        s.write(c)
        sleep(0.1)

def get_reply(s):
    reply = s.readlines()
    print ('received reply:'+ reply)
    return ''.join(reply)

def test_conn():
    s = serial.Serial(dev, timeout=1, baud)
    send_cmd(s, '$$$')
    reply = get_reply(s)
    if 'CMD' in reply:
        send_cmd(s, 'join '+ssid)
        reply = get_reply(s)
        if '...' in reply:
            return true

def main():
    if test_conn():
        
