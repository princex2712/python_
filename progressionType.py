# Write a Python program to find the type of the progression (arithmetic progression / geometric progression) and the next successive member of the three successive members of a sequence.
# According to Wikipedia, an arithmetic progression (AP) is a sequence of numbers such that the difference of any two successive members of the sequence is a constant. For instance, the sequence 3, 5, 7, 9, 11, 13, . . . is an arithmetic progression with common difference 2. For this problem, we will limit ourselves to arithmetic progression whose common difference is a non-zero integer.
# On the other hand, a geometric progression (GP) is a sequence of numbers where each term after the first is found by multiplying the previous one by a fixed non-zero number called the common ratio. For example, the sequence 2, 6, 18, 54, . . . is a geometric progression with common ratio 3. For this problem, we will limit ourselves to geometric progression whose common ratio is a non-zero integer.
def fun(arr):
    if arr[-1]==arr[-2]==arr[-3]<=0:
        return 'Wrong Numbers'
    if arr[-1]- arr[-2] == arr[-2] - arr[-3]:
        nextNum = arr[-1] - arr[-2]
        return 'Arithmetic progression, next number: {}'.format(arr[-1]+nextNum)
    elif arr[-1]/arr[-2] == arr[-2]/arr[-3]:
        nextNum = arr[-1] / arr[-2]
        return 'Geometric progression, next number: {}'.format(int(arr[-1]*nextNum))
print(fun([1, 4, 7]))
