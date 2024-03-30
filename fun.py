# Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
def fun():  
    val = [ i*i for i in range(1,31)]
    num = val[:5]+val[:-5:-1]
    return num
print(fun())
