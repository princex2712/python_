# Write a Python program that checks whether a string represents an integer or not
def fun(string):
    try:
        string=int(string)
        return string
    except:
        return 'Not a int'
def other(string):
    if all(char in '0123456789' for char in string):
        return 'Its an int'
    return 'Not a int'
print(fun('1234'))
print(other('1234'))