#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:24:20 2023

@author: frankiemalinowski
"""

#Pi = 0
#def Leibniz(n):
#    Pi = 0 
#    for N in range(n):
#        Pi += 8 / ((4*N + 1) * (4*N + 3))
#        if N == n:
 #           return print(Pi)
            
#Leibniz(100)
    
Pi = 0
for N in range(100):
    Pi += 8 / ((4*N + 1) * (4*N + 3))
    
print(Pi)
