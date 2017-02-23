#!/usr/bin/python

import socket
import subprocess
import sys

if(len(sys.argv) < 4):
	print("Usage: ./udpclient <recv_port> <send_ip> <send_port>")
	exit(1)

#read requests, send data, receive data, print data.

recv_ip = "0.0.0.0" 
recv_port = int(sys.argv[1]) #5005

send_ip = sys.argv[2] #127.0.0.1
send_port = int(sys.argv[3]) #5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((recv_ip, recv_port))

sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

while True:
	print(" >>>"),
	command = raw_input()

	sock2.sendto(command, (send_ip, send_port))


	response, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

	print(response)