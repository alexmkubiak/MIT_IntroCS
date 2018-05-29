#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 17:37:57 2018

@author: Alex
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))