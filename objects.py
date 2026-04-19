'''
OBJECTS
(1) what is object 
(2) iterable objects & Range
(3) Dictionary
(4) Error handling system

'''

import array  # package/model
import math
from math import ceil, asin

print("====== What is object =======")
# an Object has its own states and properties
# Everything is object in Python

print(type("Hello world"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional programming & OOP
# OOP 4 consepts > Abstraction | Encopsulation | Inheritance | Polymorphism

result1 = math.ceil(97.7)
print("result1:", result1)

result2 = ceil(98.7)
print("result2:", result2)
