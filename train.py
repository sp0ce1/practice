
# I-TASK (PYTHON)

# Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
# MASALAN: get_digits("m14i1t") return qiladi "141"

# Masalaga Yechim:


def get_digits(data):
    result = [x for x in data if x.isdigit()]
    return "".join(result)


print(get_digits("m14i1t"))


# G-TASK (PYTHON)

# Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.

# Masalaga Yechim:

# def get_highest_index(numbers):
#     return numbers.index(max(numbers))


# print(get_highest_index([5, 21, 12, 21, 8]))
