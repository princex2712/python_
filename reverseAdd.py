# Write a Python program to reverse the digits of a given number and add them to the original. Repeat this procedure if the sum is not a palindrome.
# Note: A palindrome is a word, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar.
def fun(num):
    new_num=str(num)
    if new_num[::-1]==new_num:
        return new_num
    while num > 0:
        temp = num%10
        new_num+=str(temp)
        num//=10
    return new_num
print(fun(56776))