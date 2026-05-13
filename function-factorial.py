def factorial(n=0):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

num = int(input('ENTER A NUMBER - '))
print(f'Factorial of {num} IS {factorial(num)}')