# Find the minimum window in a given string which will contain all the characters of another given string
def fun(string1,string2):
    start = len(string1)
    end = 0
    for char in string2:
        indx = string1.find(char)
        if indx < start:
            start = indx
        elif indx > end:
            end = indx
    return string1[start:end+1]
string1 = 'PRWSOERIUSFK'
string2 = 'OSU'
print(fun(string1,string2))
