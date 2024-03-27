# Write a Python program to compute the digit number of the sum of two given integers.
def fun(x,y):
    sum = x +y
    digit = 0
    while sum>0:
        temp = sum%10
        digit+=temp
        sum//=10
    return len(str(digit))
def simple(x,y):
    return len(str(x+y))
print(fun(5,72))
print(simple(5,72))