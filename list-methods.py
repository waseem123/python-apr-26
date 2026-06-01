mylist = ['Bottle','Pen','Duster','Computer','Screen','pen','Board','Remote','Pen']
print(mylist)
print(mylist.count('Pen'))
print('bottle' in mylist)

print(mylist.index('Computer'))
print(mylist.index('Pen'))

mylist.reverse()
print(mylist)

mylist.sort(reverse=True)
print(mylist)

demolist = ['Mike','Watch','Fan']
demolist.extend(mylist)
print(mylist)
print(demolist)

print(mylist*10)

list_a = ['C','C++','Java']
list_b = ['Python','JS']
list_c = list_b + list_a
print(list_c)

list_d = list_b*4
print(list_d)