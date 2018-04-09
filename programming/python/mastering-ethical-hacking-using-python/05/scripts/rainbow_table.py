#!/usr/bin/python

import hashlib
import sys

if len(sys.argv) != 2:
	print("[!] python " + sys.argv[0] + " list.txt")
	sys.exit()

file = sys.argv[1]

f = open(file, "r")
output = open("rainbow_table.txt", "w")
file_data = f.readlines()

for line in file_data:
	word = line.strip("\n")
	hashed_word = hashlib.sha1(word).hexdigest()
	data = "{0}: {1}".format(word, hashed_word)

	output.write(data + "\n")

output.close()