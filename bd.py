from datetime import date
DOB = date(1997, 11, 20)
today = date.today()
difference = today - DOB
print("dif",difference)
D = difference.days
print("day",D)
M = int((D/365)*12)
print("month",M)
Y = int(D/365)
print("year",Y)
