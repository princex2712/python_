def fun(list):
    for i in list:
        print('Type of {}: {}'.format(i, type(i)))

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
fun(datalist)