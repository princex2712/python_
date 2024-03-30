# Flatten a shallow list
import itertools

def fun(series):
    new_list = list(itertools.chain(*series))
    return new_list
original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
print(fun(original_list))