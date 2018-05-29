#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 11:31:39 2018

@author: Alex
"""

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmopqrstuvwxyz':
                ans = ans + c
        return ans
        
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
        return isPal(toChars(s))

print('')
print('Is eve a palindrome?')  
print(isPalindrome('true'))