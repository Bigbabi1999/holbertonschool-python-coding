#!/usr/bin/python3
"""Defines a Square class with size validation and area calculation"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes a Square instance"""
        self.size = size

    property
    def size(self):
        """Retrieve the size"""
        return self.__size

    size.setter
    def size(self, value):
        """Set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """put value in square"""
        return self.__size ** 2
