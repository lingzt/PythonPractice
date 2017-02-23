"""
Implement a function called closest_power that meets the specifications below.
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
   closest_power(3,12) returns 2
closest_power(4,12) returns 2
closest_power(4,1) returns 0

"""
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here

    exponent = 0
    if abs(base**exponent) <= abs(num) and abs(base**(exponent+1)) > abs(num): 
        print(base**exponent)
        if ((abs(num)- abs(base**exponent)) <= (abs(base**(exponent+1))-abs(num))):
            return exponent
        else:
            return exponent+1
    else:
        exponent = exponent+1
        print("___")
        print(exponent)
        
#print(closest_power(3,12))
#print(closest_power(4,12))
print(closest_power(4,16))

