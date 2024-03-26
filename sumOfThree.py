#  Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations.
import itertools
from functools import partial

X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70

def chk_sum(N,*nums):
    if sum(x for x in nums)==N:
        return (True,nums)
    else:
        return (False,nums)
pro = itertools.product(X,Y,Z)
fun = partial(chk_sum,target)
sums = set(list(itertools.starmap(fun,pro)))
for x in sums:
    if x[0]==True:
        print(x[1])