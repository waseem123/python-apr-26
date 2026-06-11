person = {
    'name':'Roger',
    'city':'Paris',
    'age':25,
    'mobileno':{'work':123456,'home':246987}
}
print(person)

person['gender'] = 'Male'
print(person)
print(person['gender'])
print(person['city'])

person.update({'qualification':'B Tech','married':False,'job':'Software Engineer'})
print(person)

print(person['mobileno']['work'])
print(person)