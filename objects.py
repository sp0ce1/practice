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

# print("====== What is object =======")
# an Object has its own states and properties
# Everything is object in Python

# print(type("Hello world"))
# print(type(100))
# print(type(True))
# print(type(array))
# print(type(math))

# Paradigm > Functional programming & OOP
# OOP 4 consepts > Abstraction | Encopsulation | Inheritance | Polymorphism

# result1 = math.ceil(97.7)
# print("result1:", result1)

# result2 = ceil(98.7)
# print("result2:", result2)


print("====== Error handling system =======")

car_dict = dict(name="Toyota", year=2026, electric=True)
# result = car_dict["origin"]
# print("result:", result)

# try:
#     print("passed here")
#     a = car_dict.speed
#     result = car_dict["origin"]
# except KeyError as err:
#     print("No origin state property found:", err)
# except AttributeError as err:
#     print("no speed found:", err)
# else:
#     print("Executed successfully without errors")
# finally:
#     print("Final closing logic")


# try:
#     print("passed here")
#     # a = car_dict.speed
#     result = car_dict["origin"]
# except (KeyError, AttributeError) as err:
#     print("No origin state property found:", err)
# else:
#     print("Executed successfully without errors")
# finally:
#     print("Final closing logic")


# General Error handling
try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
except Exception as err:
    print("General Error", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")
