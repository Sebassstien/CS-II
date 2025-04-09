__author__ = 'Sebastien LaFontaine'

import math

class Vector:
    def __init__(self, x : float = 0.0, y : float = 0.0):
        """Initializes a new vector with given x and y."""
        self.x = x
        self.y = y

    def get_x(self):
        """Returns the x-variable of the vector."""
        return self.x
        
    def get_y(self):
        """Returns the y-variable of the vector."""
        return self.y

    def set_x(self, value: float):
        """Sets the x-variable of the vector."""
        self.x = value

    def set_y(self, value: float):
        """Sets the y-variable of the vector."""
        self.y = value
    
    def __repr__(self):
        """Returns a representation of the vector."""
        return f"<{self.x:.1f}, {self.y:.1f}>"
    
    def __str__(self):
        """Returns a simplify representation of the vector."""
        return self.__repr__()

    def __eq__(self, other):
        """Check if two vectors are equal."""
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        """Adds two vectors."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Substracts two vectors."""
        return Vector(self.x - other.x, self.y - other.y)
            
    def times(self, scalar):
        """Multiplies the vector by a scalar."""
        return Vector(self.x * scalar, self.y * scalar)
    
    def distance_to(self, other):
        """Finds the distance between two vectors."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)