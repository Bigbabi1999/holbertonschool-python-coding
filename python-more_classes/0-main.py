#!/usr/bin/python3
import inspect
Rectangle = __import__('0-rectangle').Rectangle
print(inspect.getsource(Rectangle))


my_rectangle =Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
