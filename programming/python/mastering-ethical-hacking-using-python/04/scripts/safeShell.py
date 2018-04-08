#!/usr/bin/python

import os

while True:
	command = raw_input("safeShell: ~# ")
	os.system(command)