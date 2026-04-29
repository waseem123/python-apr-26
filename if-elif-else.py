a = 100
b = 200
c = 200

if a>b and a>c:
    print(f'{a} is largest')
elif b>a and b>c:
    print(f'{b} is largest')
elif c>a and c>b:
    print(f'{c} is largest')
else:
    print("VALUES ARE EQUAL")