# Write a Python program to check whether a list contains a sublist.
def sublist(li,sli):
    flag = False
    if sli == []:
        flag = True
    elif li == sli:
        flag = True
    else:
        for i in range(len(li)):
            if li[i] == sli[0]:
                n=1 
                while (n < len(sli) and li[i+n]==sli[n]):
                    n+=1
                if n == len(sli):
                    flag =True
    return flag
def issubset(l1,l2):
    flag = False
    if l1 == l2:
        flag = True
    elif l2 == []:
        flag = True
    else:
        for i in range(len(l1)):
            if l1[i] == l2[0]:
                j = 1
                while j < len(l2)  and l1[i+j] == l2[j]:
                    j+=1
                if j == len(l2):
                    flag = True
    return flag
                
a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [3, 7]

print(issubset(a, b))
print(issubset(a, c))
    