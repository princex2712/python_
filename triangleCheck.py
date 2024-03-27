# Write a Python program to check whether three given lengths (integers) of three sides form a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No".
# Input:
# Integers separated by a single space.
# 1 <= length of the side <= 1,000
# Input three integers(sides of a triangle)
# 8 6 7
# No

def is_triangle(a,b,c):
    sides = sorted([a,b,c])
    return sides[0]**2+sides[1]**2==sides[2]**2
a,b,c =map(int,input("Input three integers (sides of a triangle): ").split())

if is_triangle(a, b, c):
    print("Yes")
else:
    print("No")