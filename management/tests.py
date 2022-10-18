from django.test import TestCase






from datetime import datetime
from datetime import date
 
date_of_birth=input("Enter:")
today = date.today()

dt = datetime.strptime(date_of_birth, '%Y-%m-%d')

if dt.month<today.month:
    age=today.year-dt.year
    print(age)
elif dt.month>today.month:
        age=today.year-dt.year+1
        print(age)
elif dt.month==today.month & dt.day<today.day:
            age=today.year-dt.year-1
            print(age)
else: 
                age=today.year-dt.year-1
                print(age)

