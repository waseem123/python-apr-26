class Student:
    rollno = 101
    name = 'Waseem'
    marks = 81.45

s1 = Student()
print(s1)
print(s1.rollno)
print(s1.name)
print(s1.marks)

s2 = Student()
print(s2)
print(s2.rollno)
print(s2.name)
print(s2.marks)

s3 = Student()
s3.rollno = 102
s3.name = 'Samarth'
s3.marks = 91.99
print(s3)
print(s3.rollno)
print(s3.name)
print(s3.marks)
print('-----------------------')
students = [s1, s2, s3]
print(students)

for s in students:
    print(f'ROLL NO - {s.rollno}')
    print(f'NAME    - {s.name}')
    print(f'MARKS   - {s.marks}')
    print('_____________________')