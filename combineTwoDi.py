#  Write a Python program to combine two lists into a dictionary. The elements of the first one serve as keys and the elements of the second one serve as values. Each item in the first list must be unique and hashable.
# Sample Output:
# Original lists:
# ['a', 'b', 'c', 'd', 'e', 'f']
# [1, 2, 3, 4, 5]
# Combine the values of the said two lists into a dictionary:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
def fun(l1,l2):
    di = zip(l1,l2)
    return dict(di)
print(fun(['a', 'b', 'c', 'd', 'e', 'f'],[1, 2, 3, 4, 5]))