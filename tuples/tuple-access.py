mytuple = ('India','China','America','Japan','Germeny','Russia')
print(mytuple)

print(mytuple[0])
print(mytuple[4])
print('---------------------------')
for i in mytuple:
    print(i)
print('---------------------------')
for i in range(0,len(mytuple)):
    print(f'{i} -> {mytuple[i]}')

print('---------------------------')

print(mytuple[-1])
print(mytuple[-6])  