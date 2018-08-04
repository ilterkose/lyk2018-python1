from datetime import datetime,timedelta
import calendar
from datetime import timedelta
"""
PZT  SALI ÇARŞ PERŞ CUM CUMT PAZAR
1    2    3     4    5    6     7
8   9    10   11   11   12     13
15  16  17  18      19  20     21
"""
"""
datetime.
"""

takvim = calendar.TextCalendar(calendar.SUNDAY)
str = takvim.formatmonth(2018,7)

print(str)
