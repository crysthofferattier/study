#!/usr/bin/env python

import sys
import binascii

def vernam(msg):
	key  		= sys.argv[2]
	key_index 	= 0
	xored 		= ''

	for char in msg:
		xored += chr(ord(key[key_index % len(key)]) ^ ord(char))
		key_index += 1

	return xored

def encode(xored):
	print(binascii.hexlify(xored))


def decode(xored):
	print(xored)


def main():
	msg = sys.argv[1]
	mode = sys.argv[3]

	if mode == 'enc':
		encode(vernam(msg))
	elif mode == 'dec':
		msg = binascii.unhexlify(msg)
		decode(vernam(msg))

main()