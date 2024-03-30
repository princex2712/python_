# Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350
def fun(li):
    num = ''
    for i in li:
        num+=str(i)
    return int(num)
def simple(li):
    return int(''.join(map(str,li)))
li= [11, 33, 50]
print(fun(li))
print(simple(li))
