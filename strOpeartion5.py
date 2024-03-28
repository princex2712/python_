# Write a Python program to remove characters that have odd index values in a given string.
def fun(string):
    string = string[::2]
    return string
print(fun('abcdef'))