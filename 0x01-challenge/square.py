#!/usr/bin/python3
"""
This module defines a Square class with methods to calculate
the area and perimeter of the square.
"""

class Square():
    """A class used to represent a Square"""
    
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initialize the square with given width and height.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Calculate the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Calculate the perimeter of the square.
        
        Returns:
            int: The perimeter of the square.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Return a string representation of the square.
        
        Returns:
            str: The width and height of the square.
        """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """
    Create a square object
    """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
