#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:25:31 2023

@author: frankiemalinowski
"""

import numpy as np

def dot(a,b):
    product = np.dot(a,b)
    return print(product)

a = np.array([1,2,3])
b = np.array([6,5,4])

dot(a,b)
    