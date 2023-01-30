#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:24:54 2023

@author: frankiemalinowski
"""

import numpy as np

r = np.random.uniform(1,10,20)

#incase integers wanted instead
#r2 = np.random.randint(1,10,20)

print(r)
#print(r2)

#idx used in logical indexing to remove all numbers less than what is desired
idx = r < 5
#returns boolean array where True = <5 and False = >5
print(idx)

#takes all True values and replaces them with 0 
r[idx] = 0
print(r)