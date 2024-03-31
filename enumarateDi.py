#  Get the key, value and item in a dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print('Key  Value   Count')
for count,(key,val) in enumerate(dict_num.items(),1):
    print(f'{key}     {val}     {count}')