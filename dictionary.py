# Write a Python script to sort (ascending and descending) a dictionary by value.
def fun(dictionary):
    return dict(sorted(dictionary.items(),key=lambda x:x[1])),dict(sorted(dictionary.items(),key=lambda x:x[1],reverse=True))
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(fun(d))