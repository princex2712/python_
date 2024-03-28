#  Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
def fun(string):
    return string[len(string)-1]+string[1:-1]+string[0] 
print(fun('hello'))