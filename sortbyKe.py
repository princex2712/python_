# Write a Python program to sort a given dictionary by key.
di= {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
print(dict(sorted(di.items(),key=lambda x:x[0])))