from django.test import TestCase

# Create your tests here.


import calendar
import datetime
from datetime import timedelta

def get_start_and_end_date_from_calendar_week(year, calendar_week):       
    monday = datetime.datetime.strptime(f'{year}-{calendar_week}-1', "%Y-%W-%w").date()
    return monday, monday + datetime.timedelta(days=6.9)


x=datetime.datetime.now() - datetime.timedelta(days=((datetime.datetime.now().weekday() + 1) % 7))
y=x+datetime.timedelta(days=6)
print(y.date())
print(x.date())