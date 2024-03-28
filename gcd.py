def fun(a,b):
    if a==b:
        return a
    if a > b:
        return fun(a-b,b)
    else:
        return fun(a,b-a)
print(fun(12,14))