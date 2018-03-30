#!/usr/bin/python2.7

import socket
import sys

target = sys.argv[1]
ports = range(1, 2001)

try:
	for port in ports:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		port_status = sock.connect_ex((target, port))

		if port_status == 0:
			print "[+] The port {0} is OPEN".format(port)

		sock.close()
except socket.error as e:
	print "[!] Error!"