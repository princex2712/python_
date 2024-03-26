# Write a Python program that generates a list of all possible permutations from a given collection of distinct numbers.
import itertools

my_nums = [1, 2, 3]

perms = itertools.permutations(my_nums, 3)

for p in perms:
    print(p)
