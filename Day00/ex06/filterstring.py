# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterstring.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/08 14:59:48 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/08 15:39:17 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ft_filter import ft_filter
import sys

def filterstring(S: str, N: int) -> list:
	splitedString = S.split()
	return ft_filter(lambda word: len(word) > N, splitedString)

def main():
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