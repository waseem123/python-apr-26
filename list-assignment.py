mylist =    [65,45,65,39,45,65,78,98]
r = int(input('ENTER THE VALUE TO REMOVE - '))
o = int(input('ENTER THE OCCURANCE - '))

c = mylist.count(r)
if c>=o:
    index = 0
    for i in range(len(mylist)):
        if mylist[i] == r:
            index +=1
            if index == o:
                mylist.pop(i)
                break
else:
    print(f'DATA NOT FOUND FOR PARTICULAR OCCURANCE. Total Occurances of {r} -> {c}')
print(mylist)