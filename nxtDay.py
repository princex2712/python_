# Write a Python program to get the next day of a given date.
def fun(day,month,year):
    is_leap_year = False
    if year%400==0:
        is_leap_year=True
    elif year%100!=0 and year%4==0:
        is_leap_year=True
    
    if month in (1,3,5,7,8,10,12):
        month_days=31
    elif month==2:
        if is_leap_year:
            month_days=29
        else:
            month_days=28
    else:
        month_days=30
    if day<month_days:
        day+=1
    elif day==month_days and month==12:
        day=1
        month=1
        year+=1
    elif day==month_days and month<12:
        day=1
        month+=1
    return (day,month,year)
print(fun(29,11,2002))