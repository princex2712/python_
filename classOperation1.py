#  Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and the values of the class. Now remove the student_name attribute and display the entire attribute with values.
class Student:
    student_id = "ABC"
    student_name = "XYZ"
for arr,val in Student.__dict__.items():
    if not arr.startswith('_'):
        print(f'{arr}: {val}')
setattr(Student,'student_class','EFG ')
for arr,val in Student.__dict__.items():
    if not arr.startswith('_'):
        print(f'{arr}: {val}')
delattr(Student,'student_name')
for arr,val in Student.__dict__.items():
    if not arr.startswith('_'):
        print(f'{arr}: {val}')

