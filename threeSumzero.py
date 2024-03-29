# Write a Python class to find the three elements that sum to zero from a set of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]
def fun(series):
    res = []
    for i in range(len(series)):
        for j in range(i+1,len(series)):
            for k in range(j+1,len(series)):
                if series[i]+series[j]+series[k]==0:
                    res.append([series[i],series[j],series[k]])
    return res
print(fun([-25, -10, -7, -3, 2, 4, 8, 10]))
