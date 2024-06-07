# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/07 15:01:51 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/07 15:26:18 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import builtins
from math import isnan

def NULL_not_found(object : any) -> int:
	object_type = type(object)
	
	if object is None:
		print(f"Nothing : {object} {object_type}")
	elif object_type is builtins.float and isnan(object):
		print(f"Cheese : {object} {object_type}")
	elif object_type is builtins.int and object == 0:
		print(f"Zero : {object} {object_type}")
	elif object_type is builtins.str and object == "":
		print(f"Empty : {object_type}")
	elif object_type is builtins.bool and object == False:
		print(f"Fake : {object} {object_type}")
	else:
		print("Type not found")
		return 1
	return 0