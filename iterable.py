print("====== iterable objects & Range =======")
# Iterable objects > string dict tuple list range map filter

# text = "MIT"
# for letter in text:
#     print(f"the letter: {letter}")

# range_obj = range(3)
# print(f"range_obj:", range_obj)

# for ele in range_obj:
#     print(f"the element: {ele}")


print("====== DICTIONARY =======")

# Dictionary is JSON object
person = {"name": "Justin", "age": 25, "single": True}
person_obj = dict(name="Justin", age=25, single=True)

# print(f"the person: {person}")
# print(f"the person_obj: {person_obj}")

# Method: get()
# name = person_obj["name"]
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
# print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

del person_obj["single"]

for key in person_obj:
    print(f"the key: {key} => value {person_obj.get(key)}")
