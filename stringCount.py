# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
def fun(series):
    c = 0
    for i in series:
        if len(i)>=2 and i[0]==i[-1]:
            c+=1
    return c
series = ['abc', 'xyz', 'aba', '1221']
print(fun(series))