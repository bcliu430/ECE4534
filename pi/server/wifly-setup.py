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

def reset():
    s = serial.Serial(dev, timeout=1, baud)
    send_cmd(s, '$$$')
    reply = get_reply(s)
    if 'CMD' in reply:
        send_command('factory RESET\n')
        send_command('save\n')
        send_command('reboot\n')
    s = serial.Serial(dev, timeout=1, 9600)
    send_cmd(s, '$$$')
    if 'CMD' in reply:
        send_command('set uart baud 57600\n')
        send_command('save\n')
        send_command('reboot\n')

    s = serial.Serial(dev, timeout=1, baud)
    send_cmd(s, '$$$')
    reply = get_reply(s)
    if 'CMD' in reply:
	cmds = ['set wlan ssid'+ssid, 
                'sys autoconn 2',
                'set ip host 192.168.0.100',
                'set ip remote_port 2000',
                'set uart mode 2',
                'set wlan join 1',
                'set opt deviceid pauls_client',
                'save',
                'reboot']
        for cmd in cmds:
            semd_cmd(s,cmd)

def test_conn():
    s = serial.Serial(dev, timeout=1, baud)
    send_cmd(s, '$$$')
    reply = get_reply(s)
    if 'CMD' in reply:
        send_cmd(s, 'join '+ssid)
        reply = get_reply(s)
        if '...' in reply:
            print('connected to server')

def main():
    reset()
    test_conn()
