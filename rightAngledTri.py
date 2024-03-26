# Python: Get the third side of right angled triangle from two given sides
def pythagoras(base,height,hypotenuse):
    if base=='x':
        return "Base: {}".format((hypotenuse**2-height**2)**0.5)
    elif height=='x':
        return "Height: {}".format((hypotenuse**2-base**2)**0.5)
    elif hypotenuse=='x':
        return "Hypotenuse: {}".format((base**2+height**2)**0.5)
    else:
        return "You know the answer!"
print(pythagoras(3, 4, 'x'))
print(pythagoras(3, 'x', 5))
print(pythagoras('x', 4, 5))
print(pythagoras(3, 4, 5))