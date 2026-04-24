'''   TUPLE
(1) What is tuple: tuple vs list
(2) Unpacking arguments
(3) Zip
'''


print("========= What is tuple: tuple vs list ===============")
# Java Node.js PHP array => Python List

# literal
# numbs = [3, 5, 1, 2]
# print(numbs)

# # Constructotor
# letters = list("Hello world")
# print(letters)

# fruits = ["apple", "limon", "banana", "kiwi"]
# print("befor fruits:", fruits)

# fruits[2] = "melon"
# print("after fruits:", fruits)

# Tuple is immutable
# animals = ("dog", "cat", "fish", "lion")
# tuple_obj = ("MIT", 100, True, None)

# print(animals[0])
# # animals[0] = "bird"


print("========= Unpacking arguments ===============")

# groups = ["MIT", "FLEXY", "DEVEX", "MG"]
# x, y, z, a = groups
# print(f"the x: {x}, the y: {y}")

# avoid this -  qavs() siz ishlatmaslik
# people = "Andrew", "John"
# animals = "dog",

# groups = ["MIT", "FLEXY", "DEVEX", "MG"]
# x, y, *z = groups
# print(z)  # list


# *args > tuple

def calculate(*args):
    print("*args:", args)
    total = 1
    for x in args:
        total = total * x
    print(f"the total value: {total}")
    return total


# call
# calculate(1, 7, 2, 3)
# print("=======")
# calculate(0, 2, 300)
# print("=======")
# calculate(5, 7)


# *kwargs > dictionary


def introduce(**kwargs):
    print(f":the type(**kwargs:) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]}")


# call
# introduce(name="Justin", age=28)
# introduce(name="SHawn", age=30, single=True)


# *args with **kwargs
def greeting(*args, **kwargs):
    print("*args", args)
    print("**kwargs", kwargs)


# call
greeting("Hi", True, 10, name="John", age=22)
