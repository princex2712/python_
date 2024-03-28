#  Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.
def fun(a,b):
    if b==1:
        return a
    return a * fun(a,b-1)
print(fun(2,3))
print(fun(3,3))