#!/usr/bin/python3
"""Defines a function that check if an object is exactly an isinstance of a spcified class"""
def is_same_class(obj, a_class):
    """Return True if obj is exactly an isinstance of a_class, otherwise False"""
    return type(obj) == a_class
