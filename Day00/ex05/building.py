# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/07 21:20:56 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/07 22:29:16 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def parser(string: str):
	punctuationMarks = 0
	
	print(f" The text contains {len(string)} characters:")
	print(f"{sum(1 for c in string if c.isupper())} upper letters")
	print(f"{sum(1 for c in string if c.islower())} lower letters")
	for i in range (0, len(string)):
		if string[i] in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"):
			punctuationMarks += 1
	print(f"{punctuationMarks} punctuation marks")
	print(f"{sum(1 for c in string if c.isspace())} spaces")
	print(f"{sum(1 for c in string if c.isdigit())} digits")

def main():
	try:
		if len(sys.argv) < 2:
			try:
				stdin = input("What is the text to count?\n")
				stdin += "\n"
				parser(stdin)
			except EOFError:
				sys.exit(0)
			sys.exit(0)
		if len(sys.argv) > 2:
			raise AssertionError("Assertion Error: more than one argument is provided")
		parser(sys.argv[1])
	except AssertionError as e:
		print(e)
		sys.exit(1)
	
			

if __name__ == "__main__":
	main()