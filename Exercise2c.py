#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:10:57 2023

@author: frankiemalinowski
"""

import numpy as np

def Matrix_Multiplication(a,b):
    product = np.matmul(a,b)
    if len(a[1]) != len(b[0]):
        print('ERROR!!! INCONSISTENT DIMENSIONS')
    else:
        return print(product)

a = np.array([[1,2],[3,4,5]])
b = np.array([[1,2],[3,4]])

Matrix_Multiplication(a,b)

#print(np.dot(a[0],a[1]))