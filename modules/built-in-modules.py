import random as r

x = r.randint(1, 5)
print(x)

print(r.randrange(1,5))

otp = r.randint(1000,9999)
print(otp)

mylist = ['red','green','blue','orange']
print(mylist)

r.shuffle(mylist)
print(mylist)

print(r.choice(mylist))