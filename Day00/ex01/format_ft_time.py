# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/02 17:50:28 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/06 12:56:55 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from datetime import datetime

seconds = time.time()
print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
print(datetime.now().strftime("%B %d %Y"))