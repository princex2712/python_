# Write a Python program to count the number of characters (character frequency) in a string.
def fun(string):
    dictionary = {}
    for char in string:
        if char in dictionary:
            dictionary[char]+=1
        else:
            dictionary[char] = 1
    return dictionary
print(fun('Hello'))