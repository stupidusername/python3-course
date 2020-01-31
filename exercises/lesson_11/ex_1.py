# Requirement:
#
# Write an app that print the current time every 5 seconds.
# The format of the time must be "<hh> hours, <mm> minutes, <ss> seconds"

# Implemented on Python 3.

from datetime import datetime as dt
from time import sleep

while True:
    print(dt.now().strftime('%H hours, %M minutes, %S seconds'))
    sleep(5)
