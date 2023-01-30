#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:30:03 2023

@author: frankiemalinowski
"""

import numpy as np

def Matrix_Multiplication(a,b):
    product = np.matmul(a,b)
    return print(product)

a = np.array([[1,2],[3,4]])
b = np.array([[1,2],[3,4]])

print(a)

Matrix_Multiplication(a,b)

#print(np.dot(a[0],a[1]))