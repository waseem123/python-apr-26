class Student:
    def setData(self):
        self.name = input("Enter your name: ")
        self.sub1 = int(input("Enter marks for Subject 1: "))
        self.sub2 = int(input("Enter marks for Subject 2: "))
        self.sub3 = int(input("Enter marks for Subject 3: "))
        print('---------------------------------------')

    def getData(self):
        print(f'NAME - {self.name}')
        print(f'SUB1 - {self.sub1}')
        print(f'SUB2 - {self.sub2}')
        print(f'SUB3 - {self.sub3}')

    def getResult(self):
        self.total = self.sub1 + self.sub2 + self.sub3
        print(f'TOTAL - {self.total}')
        self.percentage = (self.total / 300) * 100
        print(f'PERCENTAGE - {self.percentage:.2f}')
        print('====================================')

stud1 = Student()
stud2 = Student()

stud1.setData()
stud2.setData()

stud1.getData()
stud1.getResult()
stud2.getData()
stud2.getResult()