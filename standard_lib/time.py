import time
from datetime import datetime, timedelta

#  time


def send_emails():
    for i in range(1000000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
# print(duration)

# datetime
dt2 = datetime.strptime("2021-08-27", "%Y-%m-%d")
dt = datetime.now() + timedelta(days=2)
date2 = datetime(2021, 8, 30)

duration = dt-date2
print("days:", duration.days)
print("second", duration.seconds)
print("total_seconds", duration.total_seconds())
