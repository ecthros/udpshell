import socket
import subprocess

#receive data, send to popen, send back

recv_ip = "127.0.0.1" 
recv_port = 5005

send_ip = "127.0.0.1"
send_port = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((recv_ip, recv_port))

sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP


while True:
	command, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

	proc = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output = proc.stdout.read() + proc.stderr.read()
	sock2.sendto(output, (send_ip, send_port))