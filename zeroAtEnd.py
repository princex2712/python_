#  Write a Python program to find the number of zeros at the end of a factorial of a given positive number.
# Range of the number(n): (1 <= n <= 2*109).
def fact(num):
    if num<=1:
        return num
    return num*fact(num-1)
def fun(num):
    fact_num = fact(num)
    count = 0
    while fact_num%10==0:
        count+=1
        fact_num//=10
    return count
print(fun(5))