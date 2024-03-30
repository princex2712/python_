# Write a Python program to generate a 3*4*6 3D array whose each element is *.
def gen():
    arr = []
    for i in range(3):
        elements = []
        for j in range(4):
            element = []
            for k in range(6):
                element.append('*')
            elements.append(element)
        arr.append(elements)
    return arr
def generate():
    arr = [[['*' for i in range(6)] for j in range(4)] for k in range(3)]
    return arr
print(gen())
print(generate())
