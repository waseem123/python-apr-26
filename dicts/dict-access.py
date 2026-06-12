employee = {
            'empId':101,
            'empName':'Aatif',
            'empSalary':55000,
            'empDesignation':'Software Lead',
            'empExperience':5
        }
print(employee)
print(f'EMPLOYEE ID          - {employee['empId']}')
print(f'EMPLOYEE NAME        - {employee['empName']}')
print(f'EMPLOYEE SALARY      - {employee['empSalary']}')
print(f'EMPLOYEE DESIGNATION - {employee['empDesignation']}')
print(f'EMPLOYEE EXPERIENCE  - {employee['empExperience']} YEARS')

print(employee.keys())
print(employee.values())
print(employee.items())
print('---------------------------------')

for x in employee:
    print(f'{x} - {employee[x]}')
print('---------------------------------')

for i in employee.keys():
    print(i)
print('---------------------------------')
for i in employee.values():
    print(i)
    
print('---------------------------------')
for i in employee.items():
    print(i)
print('---------------------------------')

for i,j in employee.items():
    print(f'{i} -> {j}')
print('---------------------------------')    

person = {
            'name': 'Sam', 
            'city': 'Solapur', 
            'age': 30, 
            'mobileno': {'work': 123456, 'home': 246987}, 
            'gender': 'Male', 
            'qual': 'B Tech'
        }

for i,j in person.items():
    if i=="mobileno":
        print(f'{i} (Work) -> {j['work']}')
    else:
        print(f'{i} -> {j}')