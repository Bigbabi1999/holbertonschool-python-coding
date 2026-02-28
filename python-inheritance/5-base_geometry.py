#!/usr/bin/python3
"""Module that defines BaseGeometry"""

class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception becausearea is not implemented"""
        raise Exception("area()is not implemented")
    def integer_validator(self, name, value):
        """Validates value as an integer"""
        if type(value) is not int:
            raise TypeError("{}must be an integer".format(name))
        
        if value <= 0:
            raise ValueError("{} must be greater then 0")