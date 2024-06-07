# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/07 15:01:51 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/07 22:50:16 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object : any) -> int:
	object_type = type(object)

	if object is None:
		print(f"Nothing : {object} {object_type}")
	elif isinstance(object, float) and object != object:
		print(f"Cheese : {object} {object_type}")
	elif isinstance(object, int) and not isinstance(object, bool) and object == 0:
		print(f"Zero : {object} {object_type}")
	elif isinstance(object, str) and object == "":
		print(f"Empty : {object_type}")
	elif isinstance(object, bool) and object == False:
		print(f"Fake : {object} {object_type}")
	else:
		print("Type not found")
		return 1
	return 0