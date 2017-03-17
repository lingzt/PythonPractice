#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:18:22 2017

@author: lingtoby
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]

'''
applyToEach(testList, timesFive)
>>> print(testList)
  [1, 4, 8, 9]
'''

def f(i):
    if i < 0:
        return -i
    else:
        return i
        
'''
  >>> print testList
  [2, -3, 9, -8]
'''
applyToEach(testList, f)