#!/usr/bin/python2.7

import urllib2
import sys

host = sys.argv[1]
dfile = sys.argv[2]

data = open(dfile, "r")
fdata = data.readlines()

for line in fdata:
	linewn = line.strip("\n")
	strreq = "{0}/{1}".format(host, linewn)

	try:
		req = urllib2.urlopen(strreq)

		if req.code == 200:
			print "[+] {0}".format(strreq)
	except Exception as e:
		pass