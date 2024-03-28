# Write a Python program to calculate the sum of a list of numbers using recursion.
def fun(series,len):
    if len<=0:
        return 0
    return series[len-1] + fun(series,len-1)
list_ = [1,2,3]
print(fun(list_,3))