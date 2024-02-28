from datetime import datetime
import pytz

time1 = pytz.timezone('Europe/Berlin')
print("Current Time is ::", datetime.now(time1))