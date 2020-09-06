import datetime
import pytz
today = datetime.date.today()
print(today)

birthday = datetime.date(2001, 2, 6)
print(birthday)

# Find days since birth
days_since_birth = (today - birthday).days
print(days_since_birth)

# Adding 10 days to current day
tdelta = datetime.timedelta(days=10)
print(today+tdelta) #or (today-tdelta)

# Friday
print(today.day)

print(today.weekday())
# Monday =0 Sunday = 6

print(datetime.time(10, 4, 6, 20))
# datetime.date (Y, M, D)
# datetime.time (H, M, S, Ms)
# datetime.date (Y, M, D, H, M, S, Ms)

# add 10 hours to current day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)

for tz in pytz.all_timezones:
    print(tz)

# string formatting with dates
# 2020-09-04 -> September 04, 2020
# strftime (f = formatting)
print(datetime_pacific.strftime("%B %d, %Y"))

#  September 04, 2020 -> 2020-09-04
# strptime (p = parsing)
datetime_thing = datetime.datetime.strptime(" September 04, 2020", '%B %d %Y')
print(datetime_thing)
