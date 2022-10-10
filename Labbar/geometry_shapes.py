from __future__ import annotations
import math


#-------------------------------SHAPE CLASS------------------------------------------------------
class Shapes: # Super klassen (överklassen)
    """Super class for Shapes"""
    def __init__ (self, x_pos: (int |float), y_pos: (int | float)):
        """main attributes"""
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __repr__(self) -> None:
        return f"{self.x_pos}{self.y_pos}"

    def __str__(self) -> None:
        return f"X-position is: {self.x_pos} and Y-position is: {self.y_pos}"

#---------------------------GETTER & SETTER X_POS--------------------------------------------   
    @property #readable
    def x_pos(self) -> int:
        return self._x_pos

    @x_pos.setter # added error handling to setter, if number isnt an int or float: error message. If input is a string: error message
    def x_pos(self, value: (int | float)): # All getters and setters have the same foundation as this one
        if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be an int or float, not {type(value)}")
        if not (0 <= value <= 10):
            raise ValueError("Number must be between 0 and 10")
        self._x_pos = value
 
    
#----------------------------GETTER & SETTER Y_POS-------------------------------------------
    @property
    def y_pos(self) -> int:
        return self._y_pos

    @y_pos.setter
    def y_pos(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be an int or float, not {type(value)}")
        if not (0 <= value <= 10):
            raise ValueError("Number must be between 0 and 10")
        self._y_pos = value  


#----------------------------OVERLOADERS-----------------------------------------------------
    def __lt__(self, other):
        """Less than"""
        return self.area < other.area

    def __gt__(self, other):
        """Greater than"""
        return self.area > other.area

    def __le__(self, other):
        """Less or equal"""
        return self.area <= other.area

    def __ge__(self, other):
        """Greater or equal"""
        return self.area >= other.area

    def __ne__(self, other): 
        """Not equal"""
        return self.area != other.area


#----------------------------MOVER------------------------------------------------------------

    def translation_mover(self, x:(int | float), y:(int |float)):
        """Moves shape from its original position"""
        if not isinstance(x, (int ,float)): # error handling for string input
            raise TypeError(f"number must be an int(whole number) or float (number with decimals)")

        if not isinstance(y, (int, float)): # error handling for string input
            raise TypeError(f"number must be an int(whole number) or float (number with decimals)")
                    
        self.x_pos += x
        self.y_pos += y

#----------------------------------------------------------------------------------------------------
#                                         CIRCLE CLASS
#----------------------------------------------------------------------------------------------------
class Circle(Shapes):
    """Circle class"""
    def __init__(self, x_pos: float, y_pos: float, radius: float):
        super().__init__(x_pos, y_pos) # what is sent up to super class
        self.radius = radius

    """String conversion for attributes Circle class"""
    def __repr__(self) -> None:
        return f"{self.x_pos}{self.y_pos}{self.radius}"

    def __str__(self) -> None: #skriv ut formen
        return f"X-position is: {self.x_pos} Y-position is: {self.y_pos} and radius is: {self.radius}"

#-----------------------------GETTER & SETTER----------------------------------------

    @property
    def circumference(self) -> (int | float):
        return 2 * math.pi * self.radius

    @circumference.setter
    def circumference(self, value: (int | float)):
        if not isinstance(value, (int, float)): 
            raise TypeError(f"Number must be an int or float, not {type(value)}")
        if not (0 <= value <= 10):
            raise ValueError("Number must be between 0 and 10")
        self._circumference = value 

    @property
    def area(self) -> (int | float):
        return math.pi * self.radius ** 2

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, value: (int | float)):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Number must be an int or float, not {type(value)}")
        if not (0 <= value <= 10):
            raise ValueError("Number must be between 0 and 10")
        self._radius = value 

#---------------------------------METHODS----------------------------------------------

    def is_unit_circle(self) -> bool: # if the circle has a radius of 1 and mid-point is in origo(x,y = 0) its a unit circle
        """Check if the circle is a unit circle"""
        return self.radius == 1 and self.x_pos == 0  and self.y_pos == 0  

    def is_inside_circle(self, x, y):
        return (x - self.x_pos)**2 + (y - self.y_pos)**2 < self.radius**2 # Source: https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle
        # calculation of euclidian distance of the new points compared to first xy points. Also has radius of circle which tells us how big the circle is.
    
    def __eq__(self, other: int | float):# Checks if the circle area is the same, if it is, it returns true
        """Check if rectangle has same area""" 
        return self.area == other

#----------------------------------------------------------------------------------------------------
#                                         RECTANGLE CLASS
#----------------------------------------------------------------------------------------------------
#FFFFFIIIIIIIIIXXXXXXAAAAAAA UML

class Rectangle(Shapes):
    """Rectangle class"""
    def __init__(self, x_pos: float, y_pos: float, base: float, height: float):
        super().__init__(x_pos, y_pos)

        self.base = base
        self.height = height

    """String conversion for attributes Rectangle class"""
    def __repr__(self) -> None:
        return f"{self.x_pos}{self.y_pos}{self.base}{self.height}"

    def __str__(self) -> None:
        return f"Rectangles X-position is: {self.x_pos} Y-position is: {self.y_pos} base is: {self.base} and height is: {self.height}"


    @property
    def base(self) -> (int | float): 
        return self._base

    @base.setter
    def base(self, value: (int | float)):
        if not isinstance(value, (int, float)): 
            raise TypeError(f"Number must be an int or float, not {type(value)}")
        if not (0 <= value <= 10):
            raise ValueError("Number must be between 0 and 10")
        self._base = value 

    @property
    def height(self) -> (int | float): 
        return self._height

    @height.setter
    def height(self, value: (int | float)):
        if not isinstance(value, (int, float)): 
            raise TypeError(f"Number must be an int or float, not {type(value)}")
        if not (0 <= value <= 10):
            raise ValueError("Number must be between 0 and 10")
        self._height = value 

    @property
    def circumference(self) -> int:
        return (self.base + self.height)**2

    @property
    def area(self) -> int:
        return self.base * self.height

#---------------------------------METHODS----------------------------------------------
    def square_checker(self) -> bool: # checks if the rectangle is a square or not
        """Checks if rectangle is a square or not"""
        if self.base == self.height: # checks if the base and height are the same measurements, if they are, its a square
            return True
        else:
            return False
    
    def is_inside_rectangle(self, x, y):
        """Checks if point is inside rectangle""" # FIXA
        if (x - self.base/2) * (y + self.height/2):
            return True
        return False
        # (x - self.x_pos)**2 + (y - self.y_pos)**2 < self.area**2 # Euclidian distance (without squareroot)


    def __eq__(self, object_2: int | float):# Checks is the area of the rectangles are the same, if so, it return True.
        """Check if rectangle has same area"""
        return self.area == object_2
