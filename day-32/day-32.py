import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

#print(day_of_week)

date_of_birth = dt.datetime(1990, 12, 28, 19)
print(date_of_birth)