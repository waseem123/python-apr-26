list_a = ['C','C++','Java']
print(list_a)

list_b = list_a
print(list_b)

list_b[2] = 'PHP'
print(list_b)
print(list_a)

list_c = list_a.copy()
print(list_c)

list_c[0] = 'Python'
print(list_c)
print(list_a)