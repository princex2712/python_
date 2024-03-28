# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def fun(a,b):
    return f"{b[0]+a[1:]} {a[0]+b[1:]}"
print(fun('xyz','abc'))