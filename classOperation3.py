# Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format.
class Student:
    school = 'AB'
    address = '2626/Z Overlook Drive, COLUMBUS'

s1 = Student()
s2 = Student()
s1.name = 'Guts'
s1.age = '12'

s2.name = 'Reyna'
s2.marks = 89
students = [s1,s2]

for student in students:
    print('\n')
    for atrr in student.__dict__:
        print(f'{atrr}:{getattr(student,atrr)}')