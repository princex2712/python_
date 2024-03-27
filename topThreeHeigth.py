#  Write a Python program to find the heights of the top three buildings in descending order from eight given buildings.
def fun(series):
    series.sort()
    return series[:-4:-1]
series = [1,2,63,52,74,35,64,2,5,24,55]
print(fun(series))