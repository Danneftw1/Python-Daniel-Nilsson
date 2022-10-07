from math import pi
import pygame
from random import randint

# Shape class, which the other (more specific) shapes inherit from
class Shape():
    def __init__(self, X: int, Y: int) -> None:
        # Readonly properties
        
        self._X = X
        self._Y = Y
        self._Area = None
        self._Circumference = None
        
        # get set
        
        self.AccelerationX = 0
        self.AccelerationY = 0
        
        self.Gravity = 1
        
        self.Color = (randint(0, 255),  # R
                      randint(0, 255),  # G
                      randint(0, 255),) # B
    
    # Readonly properies
    
    @property
    def X(self) -> int:
        return self._X
    
    @property
    def Y(self) -> int:
        return self._Y
        
    @property
    def Area(self) -> int:
        return self._Area

    @property
    def Circumference(self) -> int:
        return self._Circumference
    
    # Read/write properties
    
    @property
    def AccelerationX(self) -> int:
        return self._AccelerationX

    @AccelerationX.setter
    def AccelerationX(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("only int's are allowed!")
        self._AccelerationX = value
        
    @property
    def AccelerationY(self) -> int:
        return self._AccelerationY

    @AccelerationY.setter
    def AccelerationY(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("only int's are allowed!")
        self._AccelerationY = value
    
    
    @property
    def Gravity(self) -> int:
        return self._Gravity
    
    @Gravity.setter
    def Gravity(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("only int's are allowed!")
        self._Gravity = value
    
    
    @property
    def Color(self) -> tuple:
        return self._Color

    @Color.setter
    def Color(self, value) -> None:
        if not isinstance(value, tuple):
            raise TypeError("only tuples's are allowed!")
        self._Color = value
            
        
    # Operator overloadings.
    
    # Compare dict output of both class instances, return false if there is a missmatch
    def __eq__(self, OtherObj) -> bool:
        if self.__dict__ == OtherObj.__dict__: return True
        return False
    
    # Overloading <, <=, >, and >=.
    # Check if the first object's _Area is <, <=, >, or >= than the second ones. Return true/false.
    def __lt__(self, OtherObj) -> bool:
        if self._Area < OtherObj._Area: return True
        else: return False
        
    def __le__(self, OtherObj) -> bool:
        if self._Area <= OtherObj._Area: return True
        else: return False

    def __gt__(self, OtherObj) -> bool:
        if self._Area > OtherObj._Area: return True
        else: return False
        
    def __ge__(self, OtherObj) -> bool:
        if self._Area >= OtherObj._Area: return True
        else: return False
    
    
    # Return a dictionary containing the properties of the given class instance.
    
    def __str__(self) -> str:
        return str(self.__dict__)
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    def Translate(self, x: int, y: int) -> None:
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("only int's are allowed!")
        self._X = x
        self._Y = y
        
    def SimulateForces(self) -> None:
        self._X -= self.AccelerationX
        self._Y -= self.AccelerationY

        #self.AccelerationX -= self.Gravity
        
        self.AccelerationY = self.AccelerationY - self.Gravity



class Rectangle(Shape):
    def __init__(self, X: int, Y: int, Width: int, Height: int) -> None:
        # To propely inherit from Shape class
        super().__init__(X, Y)
        
        if not isinstance(Width, int) or not isinstance(Height, int):
            raise TypeError("only int's are allowed!")
            
        
        # Readonly properies
        
        self._Width = Width
        self._Height = Height
        
        # Caution! PEMDAS/BEDMAS's order of operation
        self._Area = Width * Height
        self._Circumference = 2 * (Width + Height)
    
    # Readonly properies
    
    @property
    def Width(self) -> None:
        return self._Width

    @property
    def Height(self) -> None:
        return self._Height
    
    
    def IsSquare(self) -> bool:
        if self._Width == self._Height: return True
        return False
    
    def IsInside(self) -> bool:
        pass


class Circle(Shape):
    def __init__(self, X: int, Y: int, Radius) -> None:
        # To propely inherit from Shape class
        super().__init__(X, Y)
        
        if not isinstance(Radius, int):
            raise TypeError("only int's are allowed!")

        # Readonly properies
        
        self._Radius = Radius
        
        # Caution! PEMDAS/BEDMAS's order of operation
        self._Area = pi * Radius ** 2
        self._Circumference = 2 * pi * Radius
        
    # Readonly property
    @property
    def Radius(self) -> None:
        return self._Radius
    
    # Check if circle is at Origo, with a radius of 1
    def IsUnitCircle(self) -> bool:
        if self._X == 0 and self._Y == 0 and self._Radius == 1: return True
        return False
    
    def IsInside(self, PointX: int, PointY: int) -> bool:
        if not isinstance(PointX, int) or not isinstance(PointY, int):
            raise TypeError("only int's are allowed!")
        
        # Source: https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle
        return (PointX - self._X)**2 + (PointY - self._Y)**2 < self._Radius**2
    
    def Draw(self, window) -> None:
        pygame.draw.circle(window, self.Color, [self._X, self._Y], self.Radius, 0)