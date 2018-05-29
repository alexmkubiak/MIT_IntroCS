#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 09:45:45 2018

isIn() function uses bisection method to determine whether or not char is in 
aStr

@author: Alex
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    x = len(aStr)
    ans = False
    
    if aStr == '':
        ans = False
    elif len(aStr) == 1:
        if char == aStr[0]:
            ans = True
        else:
            ans = False
    else:
        if char == aStr[int(x/2)]:
            ans = True
        elif char < aStr[int(x/2)]:
            aStr = aStr[:int(x/2)]
            ans = isIn(char, aStr)
        else:
            aStr = aStr[int(x/2):]
            ans = isIn(char, aStr)
    return ans

isIn('d', 'cfghilmopppqrwxyyzz')