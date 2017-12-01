#!/usr/bin/env python

import socket

from enum import Enum
import datetime

import string
from tkinter import *

class RECSTATE(Enum):
    STARTBYTE = 0
    SEQNUM = 1
    NUMBYTES = 2
    DATATYPE = 3
    DATA = 4


seqNum = b'\0x00'
numBytes = b'\0x00'
dataType = b'\0x00'
myData = [b'\0x00',b'\0x00',b'\0x00',b'\0x00',b'\0x00',b'\0x00',b'\0x00',b'\0x00']

count = b'\x00'




recState = RECSTATE.STARTBYTE

host = ''
port = 2000
size = 1


print("Running")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host, port))
s.listen()
## Connect to Wifly
clientsocket, address = s.accept()

print("Connected")

master = Tk()
master.geometry('{}x{}'.format(300,100))
master.title("Message Send")



def sendLeftTurn():
    ##TEST SEND BACK TO THE PIC CHECK WITH LA
    clientsocket.send(b'\xff')
    clientsocket.send(b'\x01')
    clientsocket.send(b'W')
    clientsocket.send(b'L') #turn left test message
    clientsocket.send(b'\xfe')
    
    clientsocket.send(b'\xff')
    clientsocket.send(b'\x01')
    clientsocket.send(b'W')
    clientsocket.send(b'L') #turn left test message
    clientsocket.send(b'\xfe')
    
    clientsocket.send(b'\xff')
    clientsocket.send(b'\x01')
    clientsocket.send(b'W')
    clientsocket.send(b'L') #turn left test message
    clientsocket.send(b'\xfe')
    
    print("SENT LEFT")
    
def sendRightTurn():
    clientsocket.send(b'\xff')
    clientsocket.send(b'\x01')
    clientsocket.send(b'W')
    clientsocket.send(b'R') #turn Right test message
    clientsocket.send(b'\xfe')
    
    clientsocket.send(b'\xff')
    clientsocket.send(b'\x01')
    clientsocket.send(b'W')
    clientsocket.send(b'R') #turn Right test message
    clientsocket.send(b'\xfe')
    
    clientsocket.send(b'\xff')
    clientsocket.send(b'\x01')
    clientsocket.send(b'W')
    clientsocket.send(b'R') #turn Right test message
    clientsocket.send(b'\xfe')
    
    print("SENT RIGHT")
    
def sendStraightTurn():
    clientsocket.send(b'\xff')
    clientsocket.send(b'\x01')
    clientsocket.send(b'W')
    clientsocket.send(b'U') #turn straight test message
    clientsocket.send(b'\xfe')
    
    clientsocket.send(b'\xff')
    clientsocket.send(b'\x01')
    clientsocket.send(b'W')
    clientsocket.send(b'U') #turn straight test message
    clientsocket.send(b'\xfe')
    
    clientsocket.send(b'\xff')
    clientsocket.send(b'\x01')
    clientsocket.send(b'W')
    clientsocket.send(b'U') #turn straight test message
    clientsocket.send(b'\xfe')
    
    print("SENT STRAIGHT")
    
def sendTurnComplete():
    ##TEST SEND BACK TO THE PIC CHECK WITH LA
    clientsocket.send(b'\xff')
    clientsocket.send(b'\x01')
    clientsocket.send(b'E')
    clientsocket.send(b'C') #turn complete message
    clientsocket.send(b'\xfe')
    
    print("SENT TURN COMPLETE")

b = Button(master, text = "Send Left Turn", command = sendLeftTurn).grid(row=0,column=0)
c = Button(master, text = "Send Turn Complete", command = sendTurnComplete).grid(row = 3, column = 0)
d = Button(master, text = "Send Right Turn", command = sendRightTurn).grid(row = 1, column = 0)
e = Button(master, text = "Send Straight Turn", command = sendStraightTurn).grid(row = 2, column = 0)
#mainloop()


## RECV Data
while 1:
    master.update()
    clientsocket.send(b'\x00') #test heart beat
    data = clientsocket.recv(size) 
    if(data):
        
        if(recState == RECSTATE.STARTBYTE):
            
            if(data == b'\xff'): 
                
                recState = RECSTATE.NUMBYTES ##SKIP SEQNUM
            
        elif(recState == RECSTATE.SEQNUM):
            seqNum = data
            recState = RECSTATE.NUMBYTES
        
        elif(recState == RECSTATE.NUMBYTES):
            numBytes = data
            recState = RECSTATE.DATATYPE
        
        
        elif(recState == RECSTATE.DATATYPE):
            dataType = data
            recState = RECSTATE.DATA
            
        elif(recState == RECSTATE.DATA):

            if(count < numBytes):
                
                idx = int.from_bytes(count, 'big', signed=False)
                
                myData[idx] = data
                count = bytes([idx + 1])
                
            elif(data == b'\xfe'): 
                recState = RECSTATE.STARTBYTE
                
                if(dataType != b'H' ):
                    print(str(numBytes)+" "+str(dataType) +" " + str(myData[0:int.from_bytes(numBytes, 'big')]))
                
                if(myData[0] == b'B'):
                    print("GOT WALL")
                    
                if(dataType ==b'P' and myData[0] == b'\x0f'):
                    print("GOT INTERSECTION")
                    
                    
                
                
                
                myData = [b'\0x00',b'\0x00',b'\0x00',b'\0x00',b'\0x00',b'\0x00',b'\0x00',b'\0x00']
                count = b'\x00'