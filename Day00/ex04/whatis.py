# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/07 15:28:38 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/07 17:14:50 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) != 2):
	print("Assertion Error: more than one argument is provided")
	sys.exit(1)

try:
	value = int(sys.argv[1])
except ValueError:
	print("Assertion Error: argument is not an integer")
	sys.exit(1)

if value % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")

