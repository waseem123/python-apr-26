n = int(input("ENTER A NUMBER - "))
temp = n
d = 0
sum = 0

# Count the digits of the number 
while temp!=0: #true
    d = d + 1  #3
    temp = temp // 10 #0

# Summation of digits raise to power of count
temp = n
while temp!=0: #True
    r = temp % 10 #1
    p = r ** d  # 1
    sum = sum + p #152 + 1 = 153
    temp = temp // 10 #0
    
# Compare the summation with original number
if sum == n:
    print(f'{n} IS AN ARMSTRONG NUMBER')
else:
    print(f'{n} IS NOT AN ARMSTRONG NUMBER')