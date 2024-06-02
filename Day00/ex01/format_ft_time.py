# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmoheyma <lmoheyma@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/02 17:50:28 by lmoheyma          #+#    #+#              #
#    Updated: 2024/06/02 17:59:10 by lmoheyma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from datetime import datetime

print(time.time())
print(datetime.now().strftime("%B %d %Y"))