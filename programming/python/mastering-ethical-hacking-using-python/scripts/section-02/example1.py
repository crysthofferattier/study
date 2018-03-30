#!/usr/bin/python2.7

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])

try:
	sock.connect((host, port))
	sock.close()
	print "[+] Connection Done!"
except socket.herror as error:
	print "[!] Connection error" + error