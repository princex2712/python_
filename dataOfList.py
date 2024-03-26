# Write a Python program to print the length of the series and the series from the given 3rd term, 3rd last term and the sum of a series.
# Sample Data:
# Input third term of the series: 3
# Input 3rd 3rd last term: 3
# Input Sum of the series: 15
# Length of the series: 5
# Series:
# 1 2 3 4 5
def fun(series):
    if len(series) < 3:
        return print("Wrong Series")
    print('Third term of the series: {}'.format(series[2]))
    print('Third 3rd last term of series: {}'.format(series[-3]))
    print('Sum of Series: {}'.format(sum(i for i in series)))
    print('Length of Series: {}'.format(len(series)))
list_= [1,2,3,4,5]
fun(list_)