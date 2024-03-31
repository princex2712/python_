# Write a Python program to remove spaces from dictionary keys.
def fun(di):
    di = {x.replace(' ',''):y for x,y in di.items()}
    print(di)
student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
fun(student_list)