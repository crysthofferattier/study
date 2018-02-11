#!/usr/bin/env python

import sys
from string import lowercase as lc

def encode_text(index, key):
	return (index + key) % 26


def decode_text(index, key):
	return (index - key) % 26


def get_file_content(file_path):
	file = open(file_path, 'r')
	text = file.read().lower()

	return text


def main():
	result 		= ''
	file_path 	= sys.argv[1]
	key  	  	= int(sys.argv[2])
	function 	= sys.argv[3]

	plain_text = get_file_content(file_path)

	for lt in plain_text:
		if lt in lc:
			index = lc.find(lt)

			if function == 'enc':
				index = encode_text(index, key)
			elif function == 'dec':
				index = decode_text(index, key)

			result += lc[index]

		else:
			result += lt

	print(result)

main()