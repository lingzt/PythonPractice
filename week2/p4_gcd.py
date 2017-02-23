# -*- coding: utf-8 -*-
"""

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. 
Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

See this website for an example of Euclid's algorithm being used to find the gcd.

Write a function gcdRecur(a, b) that implements this idea recursively. 
This function takes in two positive integers and returns one integer.
"""

def gcd(a,b):
    if a >= b:
        tempDivider = b
    else: 
        tempDivider = a
        
    while a%tempDivider != 0 or b%tempDivider != 0:
        if tempDivider == 0:
            return 1
        else:
            tempDivider -= 1
    return tempDivider



        
        


print("gcd(2, 12) " + "should be 2, and we got " + str(gcd(2, 12)))
print("gcd(6, 12) " + "should be 6, and we got " + str(gcd(6, 12)))
print("gcd(9, 12) " + "should be 3, and we got " + str(gcd(9, 12)))
print("gcd(17, 12) " + "should be 1, and we got " + str(gcd(17,12)))