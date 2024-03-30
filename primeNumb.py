# Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False
def fun(seq):
    for i in seq:
        if i == 1:
            return False
        for j in range(2,int(i**0.5)+1):
            if i%j ==0 :
                return False
    return True
print(fun([0, 3, 4, 7, 9]))
print(fun([3, 5, 7, 13]))
print(fun([2, 5, 3]))
