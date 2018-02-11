#!/usr/bin/env python

import sys
from string import uppercase as uc

def get_file_content():
	file = open(sys.argv[1], 'r')
	text = file.read().upper()
	
	return text


def frequency(text):
	lt_count = {
		'A' : 0,
		'B' : 0,
		'C' : 0,
		'D' : 0,
		'E' : 0,
		'F' : 0,
		'G' : 0,
		'H' : 0,
		'I' : 0,
		'J' : 0,
		'K' : 0,
		'L' : 0,
		'M' : 0,
		'N' : 0,
		'O' : 0,
		'P' : 0,
		'Q' : 0,
		'R' : 0,
		'S' : 0,
		'T' : 0,
		'U' : 0,
		'V' : 0,
		'W' : 0,
		'X' : 0,
		'Y' : 0,
		'Z' : 0,
	}

	for lt in text:
		if lt in uc:
			lt_count[lt] += 1

	return lt_count


def lt_order(lt_frequency):
	order = []

	for w in sorted(lt_frequency, key=lt_frequency.get, reverse=True):
		print(w + ': ' + str(lt_frequency[w]))

		order.append(w)

	return ''.join(order)


def frequency_analysis(order):
	result = common_letters(order)
	result += less_common_letters(order)


def common_letters(order):
	en_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
	score 	= 0

	for clt in en_freq[:6]:
		if clt in order[:6]:
			score += 1

	return score;


def less_common_letters(order):
	en_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
	score 	= 0

	for ult in en_freq[-6:]:
		if ult in order[-6:]:
			score += 1

	return score;


def main():
	score 		= 0

	text 	  	 	= get_file_content()
	lt_frequency 	= frequency(text)
	order 			= lt_order(lt_frequency)
	final_score 	= frequency_analysis(order)

	print('Final Score: ' + str(final_score) + ' out of 12')

main()