# Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.
def student(student_id,**kwargs):
    print(f'Student Id: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name:  {kwargs['student_name']}")
    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: {kwargs['student_name']}")
            print(f"Student Class: {kwargs['student_class']}")
student('A12')
print()
student('A12',student_name='Guts')
print()
student('A12',student_name='Guts',student_class='12')

