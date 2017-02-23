"""
Write a function to flatten a list. 
The list contains other lists, strings, or ints. 
For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

"""
def flatten(aList):
    flattened = []
    for i in aList:
        if not isinstance(i, list):
             flattened.append(i)
        else:
             flattened.extend(flatten(i))
    return flattened
    """
    for i in alist[0:]:
        flattened = []
        if isinstance(i, list):
            flatten(i)
            flattened.append(i)
            return flattened
        else:
            return alist
            """

            
                
            
            
        

"""
            aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
    """

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))

    

    
