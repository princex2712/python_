# Write a Python program to multiply all the items in a list.
def fun(series):
    if len(series)==1:
        return series[0]
    return series[-1]*fun(series[:-1])
nums = [1,2,3,4,5]
print(fun(nums))