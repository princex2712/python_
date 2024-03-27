# Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010

def fun(sequence):
    res = []
    for num in sequence:
        if int(num,base=2)%5==0:
            res.append(num)
    return res
print(fun(['0100','0011','1010','1001','1100','1001']))