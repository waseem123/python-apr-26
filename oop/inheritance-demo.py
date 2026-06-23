class Person:
    def setPersonData(self):
        self.personName = input('ENTER THE PERSON NAME: ')
        self.personAge = input('ENTER THE PERSON AGE: ')
        self.personCity = input('ENTER THE PERSON CITY: ')

    def getPersonData(self):
        print(f'PERSON NAME : {self.personName}')
        print(f'PERSON AGE  : {self.personAge}')
        print(f'PERSON CITY : {self.personCity}')

class Student(Person):
    def setStudentData(self):
        self.rollNo = int(input('ENTER THE STUDENT Roll No: '))
        self.marks = int(input('ENTER THE STUDENT MARKS: '))

    def getStudentData(self):
        print(f'STUDENT ROLL NO: {self.rollNo}')
        print(f'STUDENT MARKS: {self.marks}')

s = Student()

s.setPersonData()
s.setStudentData()
s.getPersonData()
s.getStudentData()