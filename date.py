from datetime import date
from datetime import datetime
from socket import TCP_NODELAY
from datetime import time


my_date = date(1997,11,11)
today = date.today()
print(today)
print("date as argument",my_date)

print(today.year)
print(today.month)
print(today.day)


date_time = datetime.fromtimestamp(1548515515)
print(date_time)

str = date.isoformat(today)
print(str)
print(type(str))


#####################


my_time = time(12, 14, 36)

print("Entered time", my_time)
 
# calling constructor with 1
# argument
my_time = time(minute = 14)
print("\nTime with one argument", my_time)
 
# Calling constructor with
# 0 argument
my_time = time()
print("\nTime without argument", my_time)