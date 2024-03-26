# Write a Python program to create a sequence where the first four members of the sequence are equal to one. Each successive term of the sequence is equal to the sum of the four previous ones. Find the Nth member of the sequence.
def fun(n):
    seq =[1,1,1,1]
    
    for i in range(5,n+1):
        next_num = int(seq[-1])+int(seq[-2])+int(seq[-3])+int(seq[-4])
        seq.append(next_num)
    return seq[n-1]
def fun1(n):
    if 0 < n < 5:
        return 1
    return fun1(n-1) + fun1(n-2) + fun1(n-3) + fun1(n-4)
print(fun(7))
print(fun(7))
