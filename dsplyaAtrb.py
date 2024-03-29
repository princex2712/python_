# Using function attributes display the names of all arguments
def student(student_id, student_name, student_class):
    return f"Student Id: {student_id}\nStudent Class: {student_class}\nStudent Name: {student_name}"
print(student('A12',"guts",12))