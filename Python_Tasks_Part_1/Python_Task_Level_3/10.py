import datetime



first_date_input = input('Enter First date formatted as YYYY-MM-DD: ').split('-')
last_date_input = input('Enter Second date formatted as YYYY-MM-DD: ').split('-')

year1, month1, day1 = [int(x) for x in first_date_input]
year2, month2, day2 = [int(x) for x in last_date_input]

first_date = datetime.date(year1, month1, day1)
last_date = datetime.date(year2, month2, day2)

def date_countdown(x, y):
    delta = y - x
    print(f'Difference is {delta.days} days')

date_countdown(first_date, last_date)


# My Try till i find The Answer :

'''
def date_countdown(date1, date2):
    delta = date2 - date1
    return delta.days

first_date = datetime.date(2021,10,20)
last_date = datetime.date(2022,2,20)
days = date_countdown(first_date, last_date)
print(f'Difference is {days} days')
'''

'''
def date_countdown(date1, date2):
    delta = date2 - date1
    print(f'Difference is {delta.days} days')

first_date = datetime.date(2021,10,20)
last_date = datetime.date(2022,2,20)
date_countdown(first_date, last_date)

'''




