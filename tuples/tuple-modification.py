mytuple = (1000,2000,3000,4000,5000,6000)
print(mytuple)

# mytuple.append(7000)
# print(mytuple)

# mytuple.insert(2,7000)
# print(mytuple)

# mytuple[8] = 6500
# print(mytuple)

# mytuple.pop()
# mytuple.remove()
# del mytuple[3]
# mytuple.clear()

mylist = list(mytuple)
print(mylist)
mylist.append(7000)
mylist.insert(2,6500)
mylist.pop(3)
print(mylist)
mytuple = tuple(mylist)
print(mytuple)