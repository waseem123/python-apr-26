class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getData(self):
        print(f'NAME - {self.name}')
        print(f'AGE - {self.age}')


class Employee(Person):
    def __init__(self, name, age, id, salary):
        super().__init__(name, age)
        self.id = id
        self.salary = salary

    def getData(self):
        super().getData()
        print(f'ID - {self.id}')
        print(f'SALARY - {self.salary}')


e = Employee(name='Peter', age=25, id=1, salary=20000)
e.getData()
