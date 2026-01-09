#!/usr/bin/python3
"""Defines a Square class with size validation"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """
        initializes a Square instance.

        Args:
           size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
