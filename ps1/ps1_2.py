#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:18:52 2020

@author: vicentesmacbook
"""

s = 'bobobob'
count = 0
s_len = len(s)
if s_len >= 3:
    for pos in range(0,s_len-2):
        if s[pos:pos+3] == 'bob':
            count += 1
        print(s[pos:pos+3])
print("Number of 'bob' is:",count)
