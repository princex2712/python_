# Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
import itertools
def fun(li,n):
    result = []
    for i in range(1,n+1):
        for j in li:
            temp = str(j) + str(i)
            result.append(temp)
    return result
def simple(li,n):
    new_list = ['{}{}'.format(x,y) for y in range(1,n+1) for x in li]
    return new_list
print(fun(['p','q'],5))
print(simple(['p','q'],5))