"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615

"""

n = 5
nn = str(n)+str(n)
nnn = str(n)+str(n)+str(n)

print('Result: {}'.format(n+int(nn)+int(nnn)))