#  Write a Python program to convert a month name to a number of days.
def fun(name):
    list_of_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                 'September', 'October', 'November', 'December']
    if name.title() in list_of_month:
        index = list_of_month.index(name.title())
        if index==0 or index==2 or index==4 or index==6 or index==7 or index==9 or index == 11:
            print('31 Days in {}'.format(name.title()))
        elif index==1:
            print('28/29 Days in {}'.format(name.title()))
        else:
            print('30 Days in {}'.format(name.title()))
fun('March')