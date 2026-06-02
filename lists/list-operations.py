mylist = [1000,250,500,750]
print(mylist)

n = int(input('ENTER A NEW VALUE TO INSERT IN THE LIST - '))
mylist.append(n)
print(mylist)

i = int(input('ENTER THE INDEX WHERE YOU WANT TO ADD A NEW VALUE - '))
n = int(input('ENTER A NEW VALUE TO INSERT IN THE LIST - '))
mylist.insert(i,n)
print(mylist)