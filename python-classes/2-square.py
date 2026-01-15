#!/usr/bin/python3
"""Defines a Square class with size validation"""
class Square:
    """size must be an integer"""
    def __init__(self, size=0):
        """
        Initializes a Square instance.
        Args:
           size (int): size of the square
        """
     
     def area(self):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
