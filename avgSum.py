# Python Exercise: Calculate the sum and average of n integer numbers
def fun(number):
    sum = 0
    count = 0
    while number>0:
        temp = number%10
        sum+=temp
        count+=1
        number//=10
    if count==0:
        return
    return sum/count
print(fun(12))