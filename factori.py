# Write a Python program to get the factorial of a non-negative integer using recursion.
def fun(num):
    if num <=1:
        return 1
    return num * fun(num-1)
print(fun(5))