#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:33:22 2017

@author: lingtoby
"""

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
print('\n'+'aList is ')
print(aList)
print('\n'+'bList is ')
print(bList)
print(aList==bList)
print('\n'+'aList is bList')
print(aList is bList)


a = 1
b = a
a = 3
print('\n'+'a is ')
print(a)
print('\n'+'b is ') 
print(b)
print('\n'+'a == b is ')
print(a==b)



cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)
print('\n'+'cList == dList')
print(cList == dList)
print('\n'+ 'cList is dList')
print(cList is dList)