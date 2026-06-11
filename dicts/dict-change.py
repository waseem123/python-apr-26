person = {
            'name': 'Roger', 
            'city': 'Paris', 
            'age': 25, 
            'mobileno': {'work': 123456, 'home': 246987}, 
            'gender': 'Male'
        }
print(person)
person['age'] = 29
print(person)

person.update({'name':None,'city':'Solapur','age':30,'qual':'B Tech'})
print(person)