"""
Module for recording the current date and time
"""
from datetime import datetime

# datetime object containing current date and time
_now = datetime.now()

# dd/mm/YY H:M:S
day = _now.strftime("%d")
month = _now.strftime("%m")
year = _now.strftime("%Y")
hour = _now.strftime("%H")
minutes = _now.strftime("%M")
seconds = _now.strftime("%S")
weekday = _now.weekday() # day of the week 0 being Monday and 6 being Sunday 
print(
    f"Day: {day}\nMonth: {month}\nYear: {year}\nHour: {hour}\nMinutes:"
    f" {minutes}\nSeconds: {seconds}\n Day of the week: {weekday} "
)
