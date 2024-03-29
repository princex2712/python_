# Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class.
class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def print(self):
        atrr = vars(self)
        for arr,val in atrr.items():
            print(f'{arr}:{val}')
        
s1 = Student(1,'Hello')
print('Original: ')
s1.print()
s1.std_class = 12
print('Added class:')
s1.print()
