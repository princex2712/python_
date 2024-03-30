# Write a Python program to count the number of elements in a list within a specified range.
def fun(li,min,max):
    count = 0
    for i in li:
        if min<=i<=max:
            count+=1
    return count
list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
print(fun(list1, 40, 100))
list2 = ['a', 'b', 'c', 'd', 'e', 'f']

print(fun(list2, 'a', 'e')) 