# . Write a Python program to find the key of the maximum value in a dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# Finds the key of the maximum and minimum value of the said dictionary:
# ('Roxanne', 'Theodore')

def fun(di):
    min_val = min(di.values())
    min_key = next(key for key,val in di.items() if val==min_val)        
    mx_val = max(di.values())
    mx_key = next(key for key,val in di.items() if val==mx_val)
    return min_key,mx_key
def fun1(di):
    minn = min(di,key=di.get)
    mx = max(di,key=di.get)
    return minn,mx
di = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
print(fun(di))
print(fun1(di))
