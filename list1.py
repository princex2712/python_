# Write a Python program to generate all permutations of a list in Python.
import itertools
def fun(series):
    return list(itertools.permutations(series))
print(fun([1,2,3]))