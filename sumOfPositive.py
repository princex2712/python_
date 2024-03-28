# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .
def fun(num):
    if num<=0:
        return 0
    return num + fun(num-2)
print(fun(6))