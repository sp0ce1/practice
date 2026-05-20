
'''
O-TASK (PYTHON)

Shunday function yozing, u har xil valuelardan iborat array qabul qilsin va List ichidagi sonlar yigindisini hisoblab chiqqan javobni qaytarsin.
MASALAN: calculate_summary([10, "10", {son: 10}, true, 35]) return 45
'''


def calculate_summary(data):
    total = [x for x in data if isinstance(x, int) and not isinstance(x, bool)]
    return sum(total)


result = calculate_summary([10, "10", {"son": 10}, True, 35])
print(result)


# '''
# M-TASK (PYTHON)

# Shunday function yozing, u string qabul qilsin va string palindrom yani togri oqilganda ham, orqasidan oqilganda ham bir hil oqiladigan soz ekanligini aniqlab boolean qiymat qaytarsin.
# MASALAN: palindrom_check("dad") return True;  palindrom_check("son") return False;
# '''

# # Masalaga Yechim:


# def palindrom_check(text):
#     return text == text[::-1]


# print(palindrom_check("dad"))
# print(palindrom_check("son"))


# '''
# K-TASK (PYTHON)

# Shunday function yozing, u string qabul qilsin va string ichidagi eng uzun sozni qaytarsin.
# MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan"
# '''

# Masalaga Yechim:


# def find_longest(data):
#     list = data.split()
#     return max(list, key=lambda x: len(x))


# print(find_longest("I come from Uzbekistan"))


# I-TASK (PYTHON)

# Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
# MASALAN: get_digits("m14i1t") return qiladi "141"

# Masalaga Yechim:


# def get_digits(data):
#     result = [x for x in data if x.isdigit()]
#     return "".join(result)


# print(get_digits("m14i1t"))


# G-TASK (PYTHON)

# Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.

# Masalaga Yechim:

# def get_highest_index(numbers):
#     return numbers.index(max(numbers))


# print(get_highest_index([5, 21, 12, 21, 8]))
