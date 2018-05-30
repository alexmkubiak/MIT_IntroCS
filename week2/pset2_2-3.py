#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 21:08:26 2018

@author: Alex
"""
balance = 3329
annualInterestRate = 0.2

minimumPayment = 0
localbalance = balance
while localbalance >= 0:
    localbalance = balance
    minimumPayment += 10
    localbalance = (localbalance*(1 + (annualInterestRate/12))**12) - (minimumPayment/(annualInterestRate/12))*(((1+(annualInterestRate/12))**12)-1)
    # for month in range(12):
    #     localbalance = localbalance - minimumPayment
    #     interest = (annualInterestRate/12) * localbalance
    #     localbalance += interest
    print(str(minimumPayment) + " " + str(localbalance))
print("Lowest Payment : " + str(minimumPayment))
