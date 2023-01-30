#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:15:24 2023

@author: frankiemalinowski
"""
#Q6A

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,5,500)
y = t**2 * np.exp(-2*t)

#Q6B
#mpl.rcParams.update({"text.usetex": True, "font.size" : 10})
plt.plot(t,y, linewidth = 1, color = 'red')
plt.xlabel('500 points between 0 and 5')
plt.ylabel('exponential')
plt.show()

#Q6C
Max_y = max(y)
print(Max_y)

#6D
#remove sole number of t for max_y then print
idx = y == Max_y
print(t[idx])