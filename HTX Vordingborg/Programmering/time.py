from datetime import datetime, timedelta
import time

year = int(input('Vælg år '))
month = int(input('Vælg måned '))
day = int(input('vælg dag '))
hour = int(input('Vælg time '))
minute = int(input('Vælg minut '))

targetDate = datetime(year, month, day, hour, minute)

today = datetime.today()

print(today)

print(targetDate)

print(targetDate - today)
