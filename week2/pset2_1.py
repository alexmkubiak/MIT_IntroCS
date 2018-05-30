#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 19:28:58 2018

@author: Alex
"""

balance = 3329
annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
minimumPayment = 10
for i in range(12):
    #minimumPayment = balance * monthlyPaymentRate
    balance = balance - minimumPayment
    interest = (annualInterestRate/12) * balance
    balance += interest
    print(str(minimumPayment) + "  " + str(interest) + "  " + str(balance))
    
print("Remaining balance: " + str(round(balance,2)))