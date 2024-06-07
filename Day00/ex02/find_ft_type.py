# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/06 12:58:07 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/07 22:34:17 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    if isinstance(object, list):
        print(f"List : {object_type}")
    elif isinstance(object, tuple):
        print(f"Tuple : {object_type}")
    elif isinstance(object, set):
        print(f"Set : {object_type}")
    elif isinstance(object, dict):
        print(f"Dict : {object_type}")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {object_type}")
    else:
            print("Type not found")
    return 42