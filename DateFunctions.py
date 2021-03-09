
# https://www.mytecbits.com/internet/python/first-day-of-the-month

# https://code.activestate.com/recipes/577274-subtract-or-add-a-month-to-a-datetimedate-or-datet/

import datetime

todayDate = datetime.date.today()
if todayDate.day > 25:
    todayDate += datetime.timedelta(7)
print(todayDate.replace(day=1))

from datetime import datetime, date, timedelta
todayDate = datetime.today()
todayDate = todayDate.strftime('%Y-%M-%d')
print(todayDate)

# from datetime import date
todayDate = date.today()

firstOfMonth = todayDate.replace(day=1)
print(firstOfMonth)

# from datetime import timedelta
todayDate = date(2021, 2, 16)
next_month = todayDate.replace(day=28) + timedelta(days=4)
print(next_month)
lastDayOfMonth = next_month - timedelta(days=next_month.day)
print(lastDayOfMonth)



