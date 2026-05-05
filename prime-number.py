n = 17
isPrime = True

temp = n // 2
for i in range(2,temp):
    if n%i==0:
        isPrime = False
        break

if isPrime==True:
    print(f'{n} IS PRIME')
else:
    print(f'{n} IS NOT PRIME')