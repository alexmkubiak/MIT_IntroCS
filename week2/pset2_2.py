#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 19:28:58 2018

@author: Alex
"""
balance = 3329
annualInterestRate = 0.2
#periodInterest = annualInterestRate/12
monthlyPayment = 10
#calculate balance at end of 12 months

#futureValue = (balance*(1 + periodInterest)**12) - (monthlyPayment/periodInterest)*(((1+periodInterest)**12)-1)
while (balance*(1 + (annualInterestRate/12))**12) - (monthlyPayment/(annualInterestRate/12))*(((1+(annualInterestRate/12))**12)-1) > 0:
    futureValue = (balance*(1 + (annualInterestRate/12))**12) - (monthlyPayment/(annualInterestRate/12))*(((1+(annualInterestRate/12))**12)-1)
    print(str(round(monthlyPayment)) + " " + str(round(futureValue,2)))
    monthlyPayment += 10
print("Lowest Payment: " + str(round(monthlyPayment)))


#if balance>0, add 10 to monthly payment and recalculate balance
minimumPayment = 10
while balance >= 0:
    for i in range[1:13]:
        balance = balance - minimumPayment
        interest = (annualInterestRate/12) * balance
        balance += interest
        #print(str(minimumPayment) + "  " + str(interest) + "  " + str(balance))
    minimumPayment += 10