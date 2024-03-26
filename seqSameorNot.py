"""
Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

"""
numbers = [1, 2, 3, 5, 5]

if len(numbers) == len(set(numbers)):
    print(True)
else:
    print(False)