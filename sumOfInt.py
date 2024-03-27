# Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.
def fun(x,y):
    if 15<=x+y<=20:
        return 20
    return x+y
print(fun(12,7))