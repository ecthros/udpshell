import socket
import subprocess

#read requests, send data, receive data, print data.

recv_ip = "127.0.0.1" 
recv_port = 5006

send_ip = "127.0.0.1"
send_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((recv_ip, recv_port))

sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

while True:
	print(" >>>"),
	command = raw_input()

	sock2.sendto(command, (send_ip, send_port))


	response, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

	print(response)