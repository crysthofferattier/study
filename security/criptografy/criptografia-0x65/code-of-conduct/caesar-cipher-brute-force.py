#!/usr/bin/env python

import sys
from string import lowercase as lc

def decode_text(index, key):
	return (index - key) % 26


def get_file_content(file_path):
	file = open(file_path, 'r')
	text = file.read().lower()

	return text

def caesar_cipher_brute_force(plain_text, key):
	result 		= ''

	print('Key: ' + str(key))

	for lt in plain_text:
		if lt in lc:
			index = lc.find(lt)
			index = decode_text(index, key)

			result += lc[index]
		else:
			result += lt

	print(result)

def main():
	file_path 	= sys.argv[1]

	plain_text = get_file_content(file_path)

	for key in xrange(1, 26):
		caesar_cipher_brute_force(plain_text, key)

main()