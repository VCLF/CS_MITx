#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:37:07 2020

@author: vicentesmacbook
"""

# Variables input
annual_salary = float(input('Enter your annual Salary: '))
portion_saved = float(input('Enter ther percent of your salary to save, as decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

# Variables declaration
portion_down_payment = total_cost*0.25
current_savings = 0.0
r = 0.04 # annual rate of investiment
monthly_salary = annual_salary/12
time = 0 # months needed to portion_down_payment

while current_savings < portion_down_payment:
    current_savings = current_savings*(1+r/12)+ portion_saved*monthly_salary
    time += 1

# Output messages
print('Enter your annual Salary:', int(annual_salary))
print('Enter ther percent of your salary to save, as decimal:', portion_saved)
print('Enter the cost of your dream home:', int(total_cost))
print('Number of Months:', time)