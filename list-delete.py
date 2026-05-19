mylist = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Jun','Sep','Oct','Jun','Nov','Dec']
print(mylist)

# 1.
mylist.pop()
mylist.pop()
print(mylist)

# 2.
mylist.pop(3)
print(mylist)

# 3.
mylist.remove("Jun")
mylist.remove("Jun")
print(mylist)

# 4.
del mylist[0]
print(mylist)

# 5.
mylist.clear()
print(mylist)

# 6.
del mylist
print(mylist)