# Print a dictionary in table format
my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}
for k in my_dict:
    print(k,end=' ')
print()
i=0
while i <3:
    for v in my_dict.values():
        print(v[i],end=' ')
    i+=1
    print()