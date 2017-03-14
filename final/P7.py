#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 18:47:13 2017

@author: lingtoby
"""

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    
    For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 
    1∗103+2∗102+3∗101+4∗100
    """
    
    def apply(x):
        result = 0
        for i in range(len(L)):
            result += L[i] * x**(len(L)-1-i)
        return result
    return apply

print(general_poly([1, 2, 3, 4])(10))