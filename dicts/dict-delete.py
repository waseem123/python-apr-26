person = {
            'name': 'Sam', 
            'city': 'Solapur', 
            'age': 30, 
            'mobileno': {'work': 123456, 'home': 246987}, 
            'gender': 'Male', 
            'qual': 'B Tech'
        }
print(person)
person.pop('age')
print(person)
person.popitem()
print(person)
del person['city']
print(person)
person.clear()
print(person)

del person
print(person)