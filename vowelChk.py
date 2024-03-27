# Write a Python program to check whether an alphabet is a vowel or consonant.
def fun(alpahbet):
    vowels = ['a','e','i','o','u']
    if alpahbet.lower() in vowels:
        return True
    return False
print(fun('b'))