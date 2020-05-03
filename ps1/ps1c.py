#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:37:07 2020

@author: vicentesmacbook
"""

# Variables input
annual_salary = float(input('Enter your annual Salary: '))
#portion_saved = float(input('Enter ther percent of your salary to save, as decimal: '))
#total_cost = float(input('Enter the cost of your dream home: '))
total_cost = 1000000
#semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal:'))
semi_annual_raise = 0.07
time_out = 36

# Variables declaration
portion_down_payment = total_cost*0.25
current_savings = 0.0
r = 0.04 # annual rate of investiment
monthly_salary = annual_salary/12
time = 0 # months needed to portion_down_payment
steps = 0
portion_saved = 0.4 #initial guess
erro = 101
out = 0
while abs(erro) > 100:
    
    portion_saved = portion_saved + 0.210*erro/portion_down_payment
    current_savings = 0.0
    monthly_salary = annual_salary/12
    for time in range(0,time_out+1):
        current_savings = current_savings*(1+r/12)+ portion_saved*monthly_salary
        if time%6 == 0 and time>1:
            monthly_salary *= (1+semi_annual_raise)
    erro = portion_down_payment-current_savings
    steps += 1
    if portion_saved > 1:
        out = 1
        break
    print(erro)
    

# Output messages
print('Enter your annual Salary:', int(annual_salary))
if out == 0:
    print('Best savings rate:', portion_saved)
    print('Enter the cost of your dream home:', int(total_cost))
    print('Enter the semi­annual raise, as a decimal:',semi_annual_raise)
    print('Number of Months:', time_out)
    print('Steps in bisection search:',steps)
else:
    print('It is not possible to pay the down payment in three years.')
