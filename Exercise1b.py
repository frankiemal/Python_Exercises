#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:03:00 2023

@author: frankiemalinowski
"""

from math import pi 

Pi = 0
for N in range(100):
    Pi += 8 / ((4*N + 1) * (4*N + 3))
    
print(Pi)

error = abs(pi - Pi)
print(error)