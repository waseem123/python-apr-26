# and, or, not

a = 100
b = 50
c = 70
print(a>b and a>c)
print(a<b and a>c)
print(a>b and a<c)
print(a<b and a<c)
print('-----------------------------')
a = 100
b = 50
c = 70
print(a>b or a>c)
print(a<b or a<c)
print(a>b or a<c)
print(a<b or a>c)

print(not(a>c))
print(a>b or not(a>c))
print(not(not(a>b) and not(a>c)))