#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:12:25 2023

@author: frankiemalinowski
"""
import numpy as np

a = np.array([5,4,9,2,0,4,7,2])

#Q3A
print(a[-1])

#Q3B
#prints 2nd to 5th elements as indexes start from 0 (prints index 1-5)
print(a[1:6])

#prints all elements from start to 2nd last index
print(a[:-2])

#(only integer scalar arrays can be converted to a scalar index) --- does it make it a vector??
#print(a[a::2])

#Q3C
a = a[:-1]
a = np.append(a,[9])
print(a)