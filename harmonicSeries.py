#  Write a Python program to calculate the sum of harmonic series upto n terms.
def fun(num):
    if num == 1:
        return 1
    return (1/num) + fun(num-1)
print(fun(7))
print(fun(4))