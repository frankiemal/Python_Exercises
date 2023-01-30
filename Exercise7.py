#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:51:45 2023

@author: frankiemalinowski
"""

import numpy as np

#Q7A
#PI_A = np.linalg.pinv

#Q7B
A = np.array([[1,-1], [2,4], [1,1], [3,8]])
PI_A = np.linalg.pinv(A)

#show A+ x A = inverse matrix
Ap_A = PI_A @ A
print(Ap_A)
#returns same to inverse