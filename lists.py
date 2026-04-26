''' List
(1) Working with list
(2) List methods
(3) Lambo function
(4)Enumerate, map, filter
'''

# print("======= Working with list ========= ")
# Java Node.js PHP array => Python List

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
# for team in groups:
# print(f"the team: {team}")

# constructor
letters = list("Hello world!")
# print(f"the letters: {letters} and size {len(letters)}")


# print("========")
fruits = ["apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:2]
c = fruits[::3]
d = fruits[::-1]


# print("a:", a)
# print("b:", b)
# print("c:", c)
# print("d:", d)

# print("======= list methods ========= ")
# methods > append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]

letters.append("c")  # add behind
# print(f"the append result: {letters}")

letters.insert(0, "z")  # add based on index
# print(f"the insert result: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
# print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop based on index
# print(f"the pop result2: {result2} and letters: {letters}")

# # print("=========")
# animals = ["dog", "cat", "capybara", "lion"]
# print("animals:", animals)

# animals.remove("lion")
# print("animals remove:", animals)

# del animals[0:1]
# print("animals delete:", animals)

# exist = animals.index("cat")
# print("cat exist:", exist)

# animals.clear()
# print("animals clear:", animals)

# exist2 = animals.index("cat")
# print("cat exist2:", exist2)

# if "cat" in animals:
#     print("index of cat:", animals.index("cat"))
# else:
#     print("cat does not exist")


# print("==========")
numbers = [1, 20, 12, 8, 57]

numbers.sort()
# print("sort default:", numbers)
numbers.sort(reverse=True)
# print("sort reverse:", numbers)

# immutable sorted() function and index() method
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
# print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")


# print("======= Lambda function ========= ")
# lambda is a small anonymous function
def calculate(x, y): return x * y


result = calculate(3, 5)
# print("result:", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Micheal", 30),
    ("Ali", 40)
]

people.sort()
# print("people(1)", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])
# print("people2", people)


# print("======= enumerate, map, filter ========= ")
# enumerate for index & value

# animals = ["dog", "cat", "fish"]
# for element in enumerate(animals):
#     print("element:", element)

# print("=========")
# for (index, value) in enumerate(animals):
#     print(f"the index: {index} and the value {value}")

# similar in dictionary
car_obj = dict(brand="Ferrari", year=2025)
result = car_obj.items()
# for (key, value) in result:
# print(f"the key: {key} and the value: {value}")

print("==========")
# map()
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

# new_cars = []
# for car in cars:
#     new_cars.append(car[0])
# print("new_car(1):", new_cars)

# result_map = map(lambda car: car[0], cars)
# new_cars = list(result_map)
# print("new_car(2)", new_cars)

# natija = list(map(lambda car: car[0], cars))
# print(natija)


print("==========")
# filter()

result_filter = filter(lambda car: car[1] > 80, cars)
print(list(result_filter))
