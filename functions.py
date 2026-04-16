''' 
FUNCTIONS:
(1) DEFINE vs CALL
(2) Parameter vs Argument
(3) Keyword & default arguments
(4) Scope
'''

print("=========== DEFINE (paramter) vs CALL (argument) ==============") 
# build in functions: >  print() type()
# function - reusable block of code
# instead of block {} in JAVA, Python uses : indentation.


# DEFINE - build
def greet(a):
    print(f"How do you do? {a}") 


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"

# CALL - execute 
result1 = greet("Martin")
print("result:", result1)

result2 = greeting("Justin")
print("result2:", result2)