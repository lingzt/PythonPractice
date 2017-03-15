"""
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 0.25∗n∗s2tan(π/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the regular polygon. 
The function returns the sum, rounded to 4 decimal places.

Which library should you be importing at the beginning of your code in order to call the tan 
function and to get the pi constant?
"""
import math
def polysum(n,s):
    result=0
    area=0.25*n*s**2/math.tan(math.pi/n)
    perimeter=n*s
    result = area + perimeter**2
    return round(result,4)
    
print(str(polysum(39, 45)))
print("3324595.2286")
