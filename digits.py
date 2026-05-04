n = 642
temp = n
count = 0
while temp!=0:
    count = count + 1
    temp = temp // 10

print(f'THERE ARE {count} DIGITS IN {n}')