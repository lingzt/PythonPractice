#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:35:18 2017

@author: lingtoby
"""

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        #print(L[i](x))   l 里面是所有公式
        result.append(L[i](x))
    return result
    
    
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
    
print(applyEachTo([inc, square, halve, abs], -3))
print(applyEachTo([inc, square, halve, abs], 3.0))
print(applyEachTo([inc, max, int], -3))