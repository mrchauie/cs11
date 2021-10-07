def isLeapyear(year):
    '''
    Give a year, checks the year if it's a leap year.
    Year is an integer.
    '''
    #check if year is divisible by 400 (like 2000)
    if year % 400 == 0:
        return True
    else:
        #check if year is a century
        if year % 100 == 0:
            return False
        #check if year is divisible by 4 (a normal leap year)
        else:
            if year % 4 == 0:
                return True
            else:
                return False

year_weekday_start = 2 #jan 1, 1901 starts on tuesday, sunday is 0
number_of_sundays = 0

# for year in range(1901, 2001):
#     if isLeapyear(year) == True:
#         number_of_days = 366
#     else:
#         number_of_days = 365

#     #check days of week for jan
#     for day in range(1, 32):
#         day_of_week = (year_weekday_start + day) % 7
#         # print(f'jan {day}, {year}, {day_of_week}')
#         if day_of_week == 0:
#             number_of_sundays = number_of_sundays + 1

#     #check days of week in non-jan months
#     for day in range(32, number_of_days+1):
#         day_of_week = (year_weekday_start + day) % 7

#     year_weekday_start = day_of_week


days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week_by_year = []
tDay = 0

for year in range(1901, 2001):
    if isLeapyear(year) == True:
        days_in_month[1] = 29
        days = 366
    else:
        days_in_month[1] = 28
        days = 365

    for day in range(days):
        day_of_week = (year_weekday_start + day) % 7
        day_of_week_by_year.append(day_of_week)
            
    for month in range(12):
        if day_of_week_by_year[tDay] == 0:
            number_of_sundays += 1
        tDay += days_in_month[month]
       
    #reset yearly counters
    tDay = 0
    day_of_week_by_year = []
    year_weekday_start = (day_of_week + 1) % 7

print(number_of_sundays)