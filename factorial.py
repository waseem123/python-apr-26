# 5! = 5 * 4 * 3 * 2 * 1 = 120
#    = 1 * 2 * 3 * 4 * 5 = 120

n = int(input('ENTER A NUMBER - '))
factorial = 1

for i in range(1,n+1):
    factorial = factorial * i # 24 * 5 = 120
    
print(factorial)