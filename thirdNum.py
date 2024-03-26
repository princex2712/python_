"""
Write a Python program that removes and prints every third number from a list of numbers until the list is empty.

"""
numbers = [10,20,30,40,50,60,70,80,90]
position = 3-1
inx = 0
while len(numbers)>0:
    inx = (position+inx)% len(numbers)
    print(numbers.pop(inx))
