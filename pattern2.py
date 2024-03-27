# Write a Python program to print the alphabet pattern 'E'.
# Expected Output:

#  *****                                                                  
#  *                                                                      
#  *                                                                      
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *****
for i in range(7):
    for j in range(5):
        if (i == 0 or i==3)or(j == 0 and (i==1 or i==2))or(j == 0 and (i == 4 or i==5))or i==6:
            print('*',end='')
    print()