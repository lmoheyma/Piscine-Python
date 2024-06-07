# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/06 12:58:07 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/07 15:06:23 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import builtins

def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    match object_type:
        case builtins.list:
            print(f"List : {object_type}")
        case builtins.tuple:
            print(f"Tuple : {object_type}")
        case builtins.set:
            print(f"Set : {object_type}")
        case builtins.dict:
            print(f"Dict : {object_type}")
        case builtins.str:
            print(f"{object} is in the kitchen : {object_type}")
        case _:
            print("Type not found")
    return 42
        