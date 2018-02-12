#!/usr/bin/env python

import sys
from string import lowercase as lc


def get_file_content(file_path):
	file = open(file_path, 'r')
	text = file.read().lower()

	return text


def main():
	result 		= ''
	file_path 	= sys.argv[1]
	key  	  	= sys.argv[2]
	mode	 	= sys.argv[3]

	key_index = 0

	plain_text = get_file_content(file_path)

	for lt in plain_text:
		if lt in lc:
			index = lc.find(lt)

			if mode == 'enc':
				index += lc.find(key[key_index % len(key)])
			elif mode == 'dec':
				index -= lc.find(key[key_index % len(key)])

			result += lc[index % 26]
		else:
			result += lt

	print(result)

main()