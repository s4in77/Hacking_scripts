#!/usr/bin/python3

import socket

ADDRESS= input("Target IP: ")
PORT= int(input("Target Port: "))

s = socket.socket()
s.connect((ADDRESS, PORT))
answear = s.recv(1024)
print(answear)

s.close()

