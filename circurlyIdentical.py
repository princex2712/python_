# Check whether two lists are circularly identical
def fun(l1,l2):
    print(' '.join(map(str,l1)) in ' '.join(map(str,l2*2)))
    
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
fun(list1,list2)

