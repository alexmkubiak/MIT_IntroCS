#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 11:20:19 2018

@author: Alex
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    if b == 0:
        gcd = a
    else:
        gcd = gcdRecur(b, a%b)
        
    return gcd

print(gcdRecur(9,12))