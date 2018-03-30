#!/usr/bin/python2.7

import urllib2

from urllib import urlencode

url = "http://192.168.0.104/urls/auth.php"
headers={"User-Agent" : "Scanner"}
data = {
		"username" :"askar",
		"password" : "askar"
		#"password" : "123456"
	}

data_encoded = urlencode(data)

req = urllib2.Request(url, data_encoded, headers)
final_request = urllib2.urlopen(req)
print final_request.read()