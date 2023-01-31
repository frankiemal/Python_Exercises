#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:51:45 2023

@author: frankiemalinowski
"""

import numpy as np

#Q7a
#PI_A = np.linalg.pinv

#Q7B
A = np.array([[1,-1], [2,4], [1,1], [3,8]])
PI_A = np.linalg.pinv(A)

#show A+ x A = inverse matrix
Ap_A = PI_A @ A
print(Ap_A)
#returns same to inverse

#Q7C
b = np.array([[2], [4], [6], [8]])

# A+Ax = A+(b)
# so Ix = A+(b)
x = PI_A @ b 
print(x)

#vector x = A+(b) minimises error ||Ax-b|| (||.|| = Eulidean norm)
#minimisng ||Ax-b|| known as LEAST SQUARES PROBLEM