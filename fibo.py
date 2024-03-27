# Write a Python program to get the Fibonacci series 
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

def fun(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fun(n-1) + fun(n-2)
print(fun(7))