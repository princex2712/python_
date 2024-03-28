# Write a Python program to sum recursion lists using recursion.
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21

def fun(sequence):
    total = 0
    for num in sequence:
        if type(num) == type([]):
            total +=fun(num)
        else:
            total+=num
    return total
lis=[1, 2, [3,4], [5,6]]
print(fun(lis))