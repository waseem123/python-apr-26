class EngineeringStudent:
    def setStudent(self):
        self.collegeName = input('ENTER COLLEGE NAME: ')
        self.rollNo = input('ENTER ROLL NUMBER: ')

    def getStudent(self):
        print(f'COLLEGE NAME: {self.collegeName}')
        print(f'ROLL NUMBER: {self.rollNo}')

class MechanicalStudent(EngineeringStudent):
    def setMechanicalStudent(self):
        self.specialization = input('ENTER SPECIALIZATION: ')

    def getMechanicalStudent(self):
        print(f'SPECIALIZATION: {self.specialization}')

class ComputerStudent(EngineeringStudent):
    def setComputerStudent(self):
        self.specialization = input('ENTER SPECIALIZATION: ')

    def getComputerStudent(self):
        print(f'SPECIALIZATION: {self.specialization}')

class GraduateITStudent(ComputerStudent):
    def setGraduateITStudent(self):
        self.project = input('ENTER PROJECT: ')
        self.projectDomain = input('ENTER PROJECT DOMAIN: ')
        self.marks = input('ENTER MARKS: ')
    def getGraduateITStudent(self):
        print(f'PROJECT: {self.project}')
        print(f'PROJECT DOMAIN: {self.projectDomain}')
        print(f'MARKS: {self.marks}')

# cs = ComputerStudent()
# me = MechanicalStudent()
#
# print('ENTER DATA FOR CS STUDENT')
# cs.setStudent()
# cs.setComputerStudent()
# cs.getStudent()
# cs.getComputerStudent()
# print('------------------------------')
# print('ENTER DATA FOR ME STUDENT')
# me.setStudent()
# me.setMechanicalStudent()
# me.getStudent()
# me.getMechanicalStudent()

print('------------------------------')
print('ENTER DATA FOR GRADUATED IT STUDENT')
g = GraduateITStudent()
g.setStudent()
g.setComputerStudent()
g.setGraduateITStudent()

g.getStudent()
g.getComputerStudent()
g.getGraduateITStudent()
