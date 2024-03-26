def fun(file_location):
    dictionary = {}
    with open(file_location,'r') as file:
        while True:
            char = file.read(1)
            if not char:
                break
            if char in dictionary:
                dictionary[char]+=1
            else:
                dictionary[char]=1
    return dictionary
file = 'tripletZero.py'
print(fun(file))