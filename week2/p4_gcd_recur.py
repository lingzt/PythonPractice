# -*- coding: utf-8 -*-
"""
The greatest common divisor of two positive integers is the largest integer 
that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

gcd(225, 270) = 45

48 64 = 16
64 16 = 16


A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. 
Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

See this website for an example of Euclid's algorithm being used to find the gcd.

Write a function gcdRecur(a, b) that implements this idea recursively. 
This function takes in two positive integers and returns one integer.

The greatest common divisor
"""

def gcdRecur(a, b):
    if a > b:
        (a,b) = (b,a)
    if b%a == 0:
        print("b%a == 0")
        print ("a is " + str(a))
        return a
    else:
        print("recursive")
        print ("b%a is " + str(b%a))
        print ("b is " + str(b))
        return gcdRecur(a,b%a)
        
    

print("gcdRecur(70, 160) " + "should be 10, and we got " + str(gcdRecur(70, 160)))
print("gcdRecur(6, 12) " + "should be 6, and we got " + str(gcdRecur(6, 12)))
print("gcdRecur(12, 16) " + "should be 4, and we got " + str(gcdRecur(12, 16)))
print("gcdRecur(17, 12) " + "should be 1, and we got " + str(gcdRecur(17,12)))