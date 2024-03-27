# Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
def fun(row,col):
    arrays=[]
    for i in range(row):
        array = []
        for j in range(col):
            array.append(i*j)
        arrays.append(array)
    return arrays
print(fun(2,3))
