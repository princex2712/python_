# Write a Python program to get the sum of a non-negative integer using recursion.

def fun(num):
    if num<10:
        return num
    return num%10 + fun(num//10)
print(fun(340))