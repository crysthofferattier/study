#!/usr/bin/python2.7

import socks
import socket
import urllib2

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "localhost", 9050)

req1 = urllib2.urlopen("http://api.ipify.org/?format=text")
print "The real IP is: {0}".format(req1.read())

socket.socket = socks.socksocket

req2 = urllib2.urlopen("http://api.ipify.org/?format=text")
print "The new IP is: {0}".format(req2.read())