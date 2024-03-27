# Write a Python program to print the alphabet pattern 'D'.
# Expected Output:

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  **** 
for i in range(7):
    for j in range(5):
        if i==0:
            print('*',end='')
        if 1<=i<=5 and (j==0 or j==4):
            print('*',end='   ')
        if i==6:
           print('*',end='') 
    print()