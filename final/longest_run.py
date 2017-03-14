#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
def longest_run(L):

    shiftedList = L.copy()
    baseList = [L[0]]+ L
    baseList.pop()
    compareWithPreviousItem=[]
    finalList=[]
    for i in range(len(L)):
        if shiftedList[i]>baseList[i]:
            compareWithPreviousItem.append(1)
        elif shiftedList[i]<baseList[i]:
            compareWithPreviousItem.append(-1)
        else:
            compareWithPreviousItem.append(0)
    for i in range(len(L)-1):
        subL=[L[i],L[i+1]]
        #print(subL)
        for j in range(i+1,(len(L)-1)):
            #print(compareWithPreviousItem[j] == compareWithPreviousItem[j+1])
            #print(compareWithPreviousItem[j+1]==0)
            
            if compareWithPreviousItem[j] == compareWithPreviousItem[j+1] or compareWithPreviousItem[j+1]==0 or compareWithPreviousItem[j]==0:
                subL.append(L[j+1])
            else:
                break
        finalList.append(subL)
    print(finalList)
    longest=finalList[0]
    for i in range(1,len(finalList)):
        #print(longest)
        #print(len(longest))
        #print(len(finalList[i]))
        if len(longest) < len(finalList[i]):
            longest=finalList[i]
    print(longest)
    return (sum(longest))

  
    

        
#print([10, 4, 3, 8, 3, 4, 5, 7, 7, 2])
#print(longest_run([10, 4, 3, 8, 3, 4, 5, 7,7, 7, 2]))  
#print("longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 7, 2]) returns"+ str(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 7, 2])) + " should return 33")
print(([1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(str(longest_run([1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) +" should return 65")
#print(str(longest_run([ 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))+" should return 65") 