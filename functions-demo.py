# # Function Definition
# def NAME_OF_FUNCTION(param1,param2,...paramN):
#     statement 1
#     statement 2
#     ..
#     statement N
    
# # Function Invokation / Calling
# NAME_OF_FUNCTION(value 1, value 2 ... value N)

# No parameter no return
def add():
    num1 = int(input('ENTER NUMBER - '))
    num2 = int(input('ENTER NUMBER - '))
    addition = num1 + num2
    print(addition)
    
# add()

# Parameter but no return
def subtract(a,b):
    sub = a - b
    print(sub)

# subtract(500,20)

# No parameter but return
def multiply():
    n1 = 100
    n2 = 50
    result = n1 * n2
    return result

x = multiply()
print(x)

# Parameter and return both
def division(n,d):
    return n // d

print(division(100,10))
print(division(555,10))