# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterstring.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/08 14:59:48 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/08 21:26:02 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ft_filter import ft_filter
import sys

def filterstring(S: str, N: int) -> list:
	"""
	The function output a list of words from S that have a length greater than N.
	"""
	splitedString = S.split()
	return ft_filter(lambda word: len(word) > N, splitedString)

def main():
	"""
	It uses the first argument of the pragram as string for filterstring()
	and the second argument as an int for filterstring()
	If the number of argument is different from 2, or if the type of any argument is wrong,
	it raises an AssertionError.
	
	"""
	try:
		if len(sys.argv) != 3:
			raise AssertionError("AssertionError: the arguments are bad")
		try:
			N = int(sys.argv[2])
			S = str(sys.argv[1])
			print(filterstring(S, N))
		except ValueError:
			raise AssertionError("AssertionError: the arguments are bad")
	except AssertionError as e:
		print(e)
		sys.exit(1)

if __name__ == "__main__":
	main()