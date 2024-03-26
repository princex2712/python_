# Write a Python program that accepts a positive number and subtracts from it the sum of its digits, and so on. Continue this operation until the number is positive.
def fun(num):
    while num > 0:
        num -= sum([int(i) for i in str(num)])
    return num
print(fun(8))