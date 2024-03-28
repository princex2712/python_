#  Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def fun(string):
    char= string[0]
    return char + string.replace(char,'$')[1:]
print(fun('restart'))