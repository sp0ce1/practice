''' Comprehension
(1) What is comprehension
(2) Set and dictionary comp
'''
print("==== What is comprehension =====")
# Comprehension acts like spread operator!

''' Comprehension general syntax:
a) *iterable
b) <expression> for item in iterable
c) <expression> for item in iterable <condition>
'''

# list comp.
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id((list)))


print("========")
people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0] for person in people]  # B version
print("list_people:", list_people)

print("========")
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]
list_cars = [car[0] for car in cars if car[1] > 80]
print("list_cars:", list_cars)
