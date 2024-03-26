# Write a Python program to find the total number of even or odd divisors of a given integer.
def fun(num):
    even = 0
    odd = 0
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            if i%2==0:
                even+=1
            else:
                odd+=1
    return even,odd
res = fun(6)
print('Even: ',res[0],'Odd: ',res[1])