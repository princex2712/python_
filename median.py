#  Write a Python program to find the median among three given numbers.
def median(nums):
    nums.sort()
    return nums[1]
nums = [1,29,30]
print(median(nums))