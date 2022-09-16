from datetime import date
from datetime import datetime

# my_date = date(1997,11,20)
# today = date.today()

# print(my_date)
# print(today)

 
def myAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    # month = today.month - birthDate.month  
    # day = today.day - birthDate.day
    return age
     
# Driver code
print(myAge(date(1997, 11, 20)), "years")
# print(month)
# print(day)

# month = today.month()