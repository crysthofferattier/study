#!/usr/bin/python

import sys
import hashlib

if len(sys.argv) != 2:
	print("python " + sys.argv[0] + " file.txt")


def md5(string):
	return hashlib.md5(string).hexdigest()

def sha1(string):
	return hashlib.sha1(string).hexdigest()


file = sys.argv[1]
file_data = open(file, "rb").read()
final_md5_hash = md5(file_data)
final_sha1_hash = sha1(file_data)

print(" --- File content ---")
print(file_data)

print(" --- HASH --- ")

print "MD5: {0}".format(final_md5_hash)
print "SHA1: {0}".format(final_sha1_hash)