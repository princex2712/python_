# Python: Create the combinations of 3 digit combo
nums = []

for i in range(1,10):
    for j in range(10):
        for k in range(10):
            num = str(i)+str(j)+str(k)
            print(num)
    