#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 18:00:03 2018

This code determines how many times the string 'bob' occurs in a string s.

@author: Alex
"""

s = 'azcbobobegghakl'

count = 0
index = 0
for index in s:
    if s[index] == 'b':
        if s[index + 1] == 'o':
            if s[index+2] == 'b':
                count += 1
print("Number of times bob occurs is: " + str(count))
