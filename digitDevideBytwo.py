# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
def fun():
    result = []
    for num in range(100,401):
        if num%2==0:
            num_temp = num
            digit = []
            while num>0:
                temp = num%10
                num//=10
                digit.append(temp)
            flag = True
            for i in digit:
                if i%2!=0:
                    flag = False
            if flag:
                result.append(num_temp)
    return result
def simple():
    result = []
    for i in range(100,401):
        i = str(i)
        if (int(i[0])%2==0 and int(i[1])%2==0 and int(i[2])%2==0):
            result.append(int(i))
    return result
print(fun())
print(simple())


            

