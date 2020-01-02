month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(leap_year(2019))

def month(month,year):
    if month < 1 and month > 12:
        print ('invalid month')
    if month ==2 and leap_year(year):
        return 29
    return month_days[month]

print(month(1,2020))
print (leap_year(2020))

