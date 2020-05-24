import time
from datetime import datetime

# print(datetime.datetime.now())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
