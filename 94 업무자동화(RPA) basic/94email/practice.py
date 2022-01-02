import time
print(time.strftime('%d-%b-%Y')) # 현재 날자를 일-월-연도
# %a - 요일 (Sun, Mon, Tue, ...)
# %b - 월 (Jan Feb, Mar, ...)

import datetime
dt = datetime.datetime.strptime("2020-12-30", "%Y-%m-%d")
print(type(dt))
print(dt.strftime('%d-%b-%Y'))