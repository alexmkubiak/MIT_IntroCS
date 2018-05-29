#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:27:41 2018

@author: Alex
"""
x = 100
epsilon = 1
numGuesses = 0
low = 0
high = x
ans = (high + low)/2.0

print("Please think of a number between 0 and 100!")

while abs(ans**2 - x) >= epsilon:
    print("Is your secret number " + str(ans) + "?")
    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    #user = str(input())
    try:
        if user == 'h':
            high = ans
        elif user == 'l':
            low = ans
        elif user == 'c':
            break
        else:
            raise
        ans = int((high + low) / 2.0)
    except:
        print("Sorry, I did not understand your input.")
        continue
    
print("Game over. Your secret number was " + str(ans) + ".")