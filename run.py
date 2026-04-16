# print("Hello World!") 
# print("PYTHON: Everything is object!")


# Dunder _builtins_ , _init_
message = "PYTHON: Everything is object!"
print(message)

result = type(message)

print("result:",result)

'''
    in Python, there are builtin tools:
    (1) TYPES > int, float, str, list dict
    (2) FUNCTIONS > print(), len(), input(), type(), str(), int()
    (3) CONSTANCTS > true, false, none
'''
print(dir(__builtins__))

