# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
def fun(string):
    not1 = string.find('not') 
    poor= string.find('poor')
    if not1 < poor and not1>0 and poor>0:
        string = string[:not1] + 'good' + string[poor+4:]
    return string
print(fun('The lyrics is not that poor!'))
print(fun('The lyrics is poor!'))