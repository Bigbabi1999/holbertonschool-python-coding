#!/usr/bin/python3
"""Defines a rectangle class"""

class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width = 0, height = 0):

        self.width = width
        self.height = height

    @property
    def width(self):

        return

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be > = 0")
        width = value

    @property
    def height(self):

        return

    @height.getter
    def height(self, value):

        if not isinstance(value, int):

            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be > = 0")
        height = self
