# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
# Note: There will be one solution for each input and do not use the same element twice.
# Input: numbers= [10,20,10,40,50,60,70], target=50

class Solution:
    def solution(self,series,target):
        lookup = {}
        for i,num in enumerate(series):
            if target - num in lookup:
                return (lookup[target-num],i)
            lookup[num] = i        
        
numbers= [10,20,30,40,50,60,70]
target = 50
s = Solution()
print(s.solution(numbers,target))
    