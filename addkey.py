# . Write a Python script to add a key to a dictionary.

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
dictio = {0: 10, 1: 20}
dictio.update({2:30})
print(dictio)