#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:09:43 2023

@author: frankiemalinowski
"""
import numpy as np

A = ([1,0,0,0], [1,-2,1,0], [0,1,-2,1], [0,0,0,1])
b = ([0], [1], [1], [2])

x = np.linalg.solve(A,b)
print(x)
#@ as matrix multiplication
y = (A @ x) - b 
print(y)
