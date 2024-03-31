# Write a Python program to map the values of a given list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value.
# Sample Output:
# {1: 1, 2: 4, 3: 9, 4: 16}
def fun(key,fun):
    return dict(zip(key,map(fun,key)))
print(fun([i for i in range(1,6)],lambda x:x*x*x))