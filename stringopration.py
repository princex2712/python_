# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
def fun(string):
    if len(string)<2:
        return ''
    return string[:2]+string[-2::]
print(fun('Hello'))