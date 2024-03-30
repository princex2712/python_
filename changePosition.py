# Write a Python program to change the position of every n-th value to the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
def fun(seq):
    for i in range(0,len(seq)-1,2):
        seq[i],seq[i+1] = seq[i+1],seq[i]
    return seq
seq = [0,1,2,3,4,5]
print(fun(seq))