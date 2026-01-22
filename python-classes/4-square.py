#!/usr/bin/python3
"""Just to make a Square class with size validation and area calculation"""

class Square:
    """Print a square"""

    def __init__(self, size=0):
        """Just make a Square instance"""
        self.size = size

    property
    def size(self):
        """Just the size"""
        return self.__size

    size.setter
    def size(self, value):
        """Just the size with validation"""
        if isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """put Something in square"""
        return self.__size * 2
