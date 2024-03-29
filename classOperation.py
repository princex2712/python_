# Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.
class Student:
    name = 'Terrance Morales'
    marks = 93  
print('Student Name: ',getattr(Student,'name'))
print('Student Marks: ',getattr(Student,'marks'))
setattr(Student,'name','Prince')
setattr(Student,'marks',89)
print('Student Name: ',getattr(Student,'name'))
print('Student Marks: ',getattr(Student,'marks'))

