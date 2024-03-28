#  Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
def fun(series):
    return sorted(set(series))
series = ['green','red','black','white'] 
print(fun(series))