# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tester.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/08 16:37:13 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/08 21:11:46 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
	sleep(0.005)
print()

# for elem in tqdm(range(333)):
# 	sleep(0.005)
# print()