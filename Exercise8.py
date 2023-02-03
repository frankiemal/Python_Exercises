#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 18:33:24 2023

@author: frankiemalinowski
"""

from math import pi 

#Pi = 0
#for N in range(100):
#    Pi += 8 / ((4*N + 1) * (4*N + 3))
    
#print(Pi)

#error = abs(pi - Pi)
#print(error)

#error = pi - Pi
#so 10^-7 > pi - Pi 
#Pi < pi - 10^-7

Pi = 0
for N in range(100000000):
    Pi += 8 / ((4*N + 1) * (4*N + 3))
    error = abs(pi-Pi)
    
    if error == 10^-7:
        break 
        print(f'The value on N to produce an error < 10^-7 is {N}')
    else:
        continue


print(Pi)
print(error)

    