#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 11:09:15 2018

@author: Alex
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
        gcd = a
    else:
        gcd = b
    
    while gcd > 1:
        if a%gcd == 0 and b%gcd == 0:
            break
        else:
            gcd -= 1
        
    return gcd

print(gcdIter(9,12))