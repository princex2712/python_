def fun(nums):
    result = []
    for i in range(0,10):
        if i not in nums:
            result.append(i)
    return result
print(fun([9, 8, 3, 2, 2, 0, 9, 7, 6, 3]))