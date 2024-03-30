# Write a Python function that takes two lists and returns True if they have at least one common member
def fun(l1,l2):
    lx = l1 if len(l1)<len(l2) else l2
    ly = l2 if len(l1)<len(l2) else l1
    for i in lx:
        if i in ly:
            return True
    return False

l1 = [1,2,3,4,5,6,7,8,10]
l2 = [9,11]
print(fun(l1,l2))
