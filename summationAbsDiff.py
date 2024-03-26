# Write a Python program to compute the summation of the absolute difference of all distinct pairs in a given array (non-decreasing order).
# Sample array: [1, 2, 3]
# Then all the distinct pairs will be:
# 1 2
# 1 3
# 2 3
def fun(arr):
    n = len(arr)
    total_sum= 0
    for i in range(n-1):
        for j in range(i+1,n):
            total_sum+=arr[j]-arr[i]
    return total_sum
print(fun([1,2,3]))