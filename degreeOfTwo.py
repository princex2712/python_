# Write a Python program that finds the value of n when n degrees of number 2 are written sequentially on a line without spaces between them.
def fun(num):
    temp = 2
    i=2
    flag = True
    while flag:
        if str(temp) in num:
            temp = pow(2,i)
            i+=1
        else:
            flag= False
    return i - 2

print(fun('24816'))