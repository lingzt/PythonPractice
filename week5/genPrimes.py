#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:42:28 2017

@author: lingtoby
"""

def genPrimes():
    number = 2
    while True:
        number +=1
        if isPrime(number):
            prime = number
            yield prime
            
def isPrime(aNumber):
    for divider in range(1,aNumber):
        if aNumber% divider != 0:
            return False
        return True