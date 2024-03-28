# Write a Python program to calculate the geometric sum up to 'n' terms.
def fun(num):
    if num == 0:
        return 1
    return 1/pow(2,num) + fun(num-1)
print(fun(7))
print(fun(4))