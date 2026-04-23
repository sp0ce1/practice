'''
LOOP operators:
   for
   break/else
   while

'''
# print("===== for operator =======")
# Iterable objects > string dict tuple list range map filter

text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="Ferrari", year=2026)
range_obj = range(5)

# for letter in text:
#     print(f"the letter: {letter}")

# print("=========")
# for number in numbs:
#     print(f"the number: {number}")

# print("=========")
# for x in range_obj:
#     print(f"the element: {x}")

# print("=========")
# for key in car_obj:
#     print(f"the key: {key} => value {car_obj.get(key)}")

# for key, value in car_obj.items():
#     print(f"the key: {key} {value}")

# print("=========")
# for x in range(1, 20, 5):
#     print(f"the x: {x}")


# print("===== break/else =======")
# for x in range(1, 20, 5):
#     print(f"the x: {x}")
#     if x > 10:
#         print("Reached break")
#         break
#     else:
#         print("Looped successfully")


# print("===== while operator =======")
# numb = 40
# while numb > 0:
#     numb -= 10
#     print(f"the numb equal: {numb}")


print("=========")

count = 0
while True:
    count += 1
    x = int(input("find number"))

    if x == 41:
        print(f"you found the number in {count} step")
        break
    else:
        print("wrong, please find again")
