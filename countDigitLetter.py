# Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2
def fun(string):
    digit = 0
    letter = 0
    for i in string:
        if 48<= ord(i) <=57:
            digit+=1
        elif 65<=ord(i)<=90 or 97<=ord(i)<=122:
            letter+=1
    return digit,letter
print(fun('W3resource'))