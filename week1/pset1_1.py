#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 21:46:18 2018

This code counts the number of vowels that occur in string s.

@author: Alex
"""

i = 0
vowels = 0
while i < len(s):
    if s[i] == 'a':
        vowels += 1
        i += 1
    elif s[i] == 'e':
        vowels += 1
        i += 1
    elif s[i] == 'i':
        vowels += 1
        i += 1
    elif s[i] == 'o':
        vowels += 1
        i += 1   
    elif s[i] == 'u':
        vowels += 1
        i += 1
    else:
        i += 1
        
print ("Number of vowels: "+ str(vowels))