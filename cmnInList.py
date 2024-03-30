# Write a Python program to find common items in two lists.
def fun(l1,l2):
    return set(l1) & set(l2)
a = [1,2,3,4,5]
b = [4,5,6,7,9] 
print(fun(a,b))