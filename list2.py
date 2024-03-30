# Difference between the two lists
def fun(l1,l2):
    list1 = list(set(l1) - set(l2))
    list2 = list(set(l2) - set(l1))
    return list1+list2
list1 = [1, 3, 5, 7, 9]

# Define another list 'list2' containing different numbers
list2 = [1, 2, 4, 6, 7, 8]
print(fun(list1,list2))