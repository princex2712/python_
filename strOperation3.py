# Write a Python program to remove the nth index character from a nonempty string.
def fun(string,n):
    return string[:n]+string[n+1:]
print(fun('Python',2))