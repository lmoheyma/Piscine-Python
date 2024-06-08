# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/08 16:36:52 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/08 21:31:37 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_tqdm(lst: range):
	"""
	It reproduces the comportment of the function tqdm
	It shows pourcent and a loading bar
	"""
	count = len(lst)
	def show(j):
		x = int(85 * j / count)
		print(f"{(j/count) * 100:.0f}%|{u'█'*x}{('.'*(85 - x))}| {j}/{count}", end='\r', flush=True)
	show(0.1)
	for i, item in enumerate(lst):
		yield item
		show(i + 1)