# from datetime import datetime
# from datetime import date
# from dateutil import relativedelta

# date_of_birth = input("enter")
# birth=datetime.strptime(str(date_of_birth), '%Y-%m-%d')

# current = datetime.now() # July 27th, 2020 at the time of writing

# print(current-birth)
# diff=relativedelta.relativedelta(current, birth)
# print(diff)
# if diff.years > 0:
#     print(f'{diff.years} years')
# elif diff.months >0:
#     print(f'{diff.months} months')
# elif diff.days >0:
#     print(f'{diff.days} days')
# elif diff.hours >0:
#     print(f'{diff.hours} hours')

# day_answer = current.day - birth.day
# month_answer = current.month - birth.month
# year_answer = current.year - birth.year

# if day_answer<0:
#     month_answer-=1
#     day_answer+=31

# if month_answer < 0:
#     year_answer -=1
#     month_answer += 12
    
# print(year_answer, month_answer, day_answer)
# date_of_birth = input("enter")
# birth=datetime.strptime(str(date_of_birth), '%Y-%m-%d')
                
# current = date.today() # July 27th, 2020 at the time of writing
# diff=relativedelta.relativedelta(current, birth)
# if diff.years > 0:
#     return f'{diff.years} years'
# elif diff.months >0:
#     return f'{diff.months} months'
# elif diff.days >0:
#     return f'{diff.days} days'
# elif diff.hours >0:
#     return f'{diff.hours} hours'

x=[3,4]
y=[4,6]
t=zip(x,y)
print(t)
