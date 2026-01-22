#!/usr/bin/python3
"""Just to make a Square class with size validation and area calculation"""


class Square:
    """Print a square"""

    def __init__(self, size=0):
        """Just make a Square instance"""
        self.size = size

    @property
    def size(self):
        """Just the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Just the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using #"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
