#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:40:18 2020

@author: vicentesmacbook
"""

# Demand an input.
print("Please think of a number between 0 and 100!")
# Ask for opinion
low = 0
high = 100
guess = 50
ans = 'a'
while ans != 'c':
    print('Is your secret number',guess,' ?')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if (ans != 'h' and ans != 'l' and ans != 'c'):
        print('Sorry, I did not understand your input.')
    elif ans == 'h':
        high = guess
        guess = round((high + low)/2)
    elif ans == 'l':
        low = guess
        guess = round((high + low)/2)
print('Game over. Your secret number was:',guess)
        