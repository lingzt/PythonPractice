#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 21:54:40 2017

@author: lingtoby
"""


          
def convert_to_mandarin(us_num):
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    '''
There are words for each of the digits from 0 to 10.
For numbers 11-19, the number is pronounced as "ten digit", 
so for example, 16 would be pronounced (using Mandarin) as "ten six".
For numbers between 20 and 99, the number is pronounced 
as “digit ten digit”, so for example, 37 would be pronounced (using Mandarin) 
as "three ten seven". If the digit is a zero, it is not included.
    '''
    num = int(us_num)
    mandarinString = ""
    if num == 0:
        onesString = "ling"
    elif num %10 ==0:
        onesString = ""
    else:
        onesString = trans[str(num %10)]
    if int(num/10) == 0:
        tensString = ""
    else:
        if int(num/10) == 1:
            tensString = "shi"
        else: 
            tensString = trans[str(int(num/10))] + " shi"
        if onesString != "":
            tensString += " "
            
    mandarinString = tensString+onesString 
    return mandarinString
print("convert_to_mandarin('1') returns"+ convert_to_mandarin('1') + " should return yi")
print("convert_to_mandarin('36') returns "+convert_to_mandarin('36') + " should return san shi liu")
print("convert_to_mandarin('20') returns" +convert_to_mandarin('20') + " should return er shi")
print("convert_to_mandarin('16') returns" +convert_to_mandarin('16') + " should return shi liu")
print("convert_to_mandarin('0') returns" +convert_to_mandarin('0') + " should return ling")