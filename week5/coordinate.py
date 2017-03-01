"""
Add an __eq__ method that returns True if coordinates refer to same point in the plane 
(i.e., have the same x and y coordinate).

Define __repr__, a special method that returns a string that looks like a valid Python expression 
that could be used to recreate an object with the same value. 
In other words, eval(repr(c)) == c given the definition of __eq__ from part 1.

For more on __repr__, see this SO post.
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, other): #make sure double underscore being used on both sides
        assert type(other) == type(self) #make sure the type is the same. 
        if self.x == other.x and self.y == other.y :
            return True
        else:
            return False
#Example: 'datetime.date(2009, 1, 16)'
    def __repr__(self):
        aStr = 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
        return aStr
        
c1 = Coordinate(1,-8)

c2 = Coordinate(1,-8)

print(c1 == c2)

