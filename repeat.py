import time
from datetime import datetime
from auto import press
import random

# Check daytime
weekdays = [1, 2, 3, 4, 5]
hh1 = 8
mm1 = 20 + int(random.uniform(0, 20))  #8:20~8:40
hh2 = 17
mm2 = 40 + int(random.uniform(1, 16))  #17:40+
print(f"next: {hh1}:{mm1} ,{hh2}:{mm2}")

while True:
    now = datetime.now()
    c_time = (now.hour, now.minute)
 
    if now.weekday() in weekdays and (c_time == (hh1, mm1) or c_time == (hh2, mm2)):
        press()
        if now.hour == hh1:
            mm1 = 20 + int(random.uniform(0, 20))
        else:
            mm2 = 40 + int(random.uniform(1, 16))

        time.sleep(60*20)
    else:
        time.sleep(10)