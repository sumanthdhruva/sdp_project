import calendar
import datetime
import time
print(time.time())
print(time.asctime())

datetime_object = datetime.datetime.now()
print(datetime_object)
print("Year::", datetime_object.year)

s = calendar.prcal(3023)
s2 = calendar.month(2004,12)
s1 = calendar.isleap(2004)
print(s1)
print(s2)

x = datetime.datetime.now()
print(x + datetime.timedelta(days = -1))

