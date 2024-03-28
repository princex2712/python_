# Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
def fun(string):
    dictionary = {key:string.count(key) for key in string if string.count(key)>1}
    return dictionary
print(fun('thequickbrownfoxjumpsoverthelazydog'))