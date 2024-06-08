# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/07 22:57:43 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/08 15:17:03 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def is_even(nb: int) -> bool:
	if nb % 2 == 0:
		return True
	return False

def ft_filter(function, iterable) -> list:
	if function:
		return [item for item in iterable if function(item)]
	else:
		return [item for item in iterable if item]
			
def main():
	nb_list = [5, 8, 65, 3, 4, 90, 48, 2, 6]
	print(ft_filter(is_even, nb_list))

if __name__ == "__main__":
	main()