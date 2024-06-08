# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/08 15:41:36 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/08 16:33:49 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def stringToMorse(string: str) -> str:
	NESTED_MORSE = {" ": "/",
		"A": ".-",
		"B": "-...",
		"C": "-.-.", 
		"D": "-..", 
		"E": ".",
		"F": "..-.", 
		"G": "--.", 
		"H": "....",
		"I": "..",
		"J": ".---",
		"K": "-.-",
		"L": ".-..",
		"M": "--",
		"N": "-.",
		"O": "---",
		"P": ".--.",
		"Q": "--.-",
		"R": ".-.",
		"S": "...",
		"T": "-",
		"U": "..-",
		"V": "...-",
		"W": ".--",
		"X": "-..-",
		"Y": "-.--",
		"Z": "--..",
		"1": ".----",
		"2": "..---",
		"3": "...--",
		"4": "....-",
		"5": ".....",
		"6": "-....",
		"7": "--...",
		"8": "---..",
		"9": "----.",
		"0": "-----"}
	i = 0
	for letter in string:
		print(NESTED_MORSE[letter.upper()], end="")
		if i != len(string) - 1:
			print(" ", end="")
		else:
			print("")
		i += 1

def main():
	try:
		if len(sys.argv) != 2:
			raise AssertionError("AssertionError: the arguments are bad")
		try:
			string = str(sys.argv[1])
			for letter in string:
				if not letter.isalnum() and not letter.isspace():
					raise AssertionError("AssertionError: the arguments are bad")
			stringToMorse(string)
		except ValueError: 
			raise AssertionError("AssertionError: the arguments are bad")
	except AssertionError as e:
		print(e)
		sys.exit(1)
	
if __name__ == "__main__":
	main()