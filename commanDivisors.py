# Write a Python program to find common divisors between two numbers in a given pair.
def fun(pair):
    min_num = min(pair)
    res = []
    for i in range(1,int(min_num**0.5)+1):
        if pair[0]%i==0 and pair[1]%i==0:
            res.append(i)
    return res
print(fun([2,4]))
def common_divisors(pair):
    min_num = min(pair)
    res = []
    sqrt_min = int(min_num ** 0.5)
    for i in range(1, sqrt_min + 1):
        if pair[0] % i == 0 and pair[1] % i == 0:
            res.append(i)
            if i != min_num // i:  
                res.append(min_num // i)
    return res

print(common_divisors([2, 4]))
