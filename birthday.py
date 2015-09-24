"""
birthday.py
Author: Jasmine Lou
Credit: The internet and classmates, and teachers
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
tday = str(todaydate)
tmonth = str(todaymonth)

name = input("Hello, what is your name? ")
month = input("Hi "+ name + ", what was the name of the month you were born in? ")
month = month.lower()
year = input("And what year were you born in, " + name + "? ")
day = input("And the day? ")

if tmonth==month and tday==day:
    print("Happy birthday!")

if month == "october" and day == "31":
    print("You were born on Halloween!")
elif int(year) < int(1980) and month == "september":
    print("You are a fall baby of the stone age.")
elif int(year) < int(1980) and month == "october":
    print("You are a fall baby of the stone age.")
elif int(year) < int(1980) and month == "november":
    print("You are a fall baby of the stone age.")
elif int(year) < int(1980) and month == "december":
    print("You are a winter baby of the stone age.")
elif int(year) < int(1980) and month == "january":
    print("You are a winter baby of the stone age.")
elif int(year) < int(1980) and month == "february":
    print("You are a winter baby of the stone age.")
elif int(year) < int(1980) and month == "march":
    print("You are a spring baby of the stone age.")
elif int(year) < int(1980) and month == "april":
    print("You are a spring baby of the stone age.")
elif int(year) < int(1980) and month == "may":
    print("You are a spring baby of the stone age.")
elif int(year) < int(1980) and month == "june":
    print("You are a summer baby of the stone age.")
elif int(year) < int(1980) and month == "july":
    print("You are a summer baby of the stone age.")
elif int(year) < int(1980) and month == "august":
    print("You are a summer baby of the stone age.")
elif int(1980) <= int(year) < int(1990) and month == "september" or month == "october" or month == "november":
    print("You are a fall baby of the eighties.")
elif int(1980) <= int(year) < int(1990) and month == "december" or month == "january" or month == "february":
    print("You are a winter baby of the eighties.")
elif int(1980) <= int(year) < int(1990) and month == "march" or month == "april" or month == "may":
    print("You are a spring baby of the eighties.")
elif int(1980) <= int(year) < int(1990) and month == "june" or month == "july" or month == "august":
    print("You are a summer baby of the eighties.")
elif int(1990) <= int(year) < int(2000) and month == "september" or month == "october" or month == "november":
    print("You are a fall baby of the nineties.")
elif int(1990) <= int(year) < int(2000) and month == "december" or month == "january" or month == "february":
    print("You are a winter baby of the nineties.")
elif int(1990) <= int(year) < int(2000) and month == "march" or month == "april" or month == "may":
    print("You are a spring baby of the nineties.")
elif int(1990) <= int(year) < int(2000) and month == "june" or month == "july" or month == "august":
    print("You are a summer baby of the nineties.")
elif int(2000) <= int(year) and month == "september" or month == "october" or month == "november":
    print("You are a fall baby of the two thousands.")
elif int(2000) <= int(year) and month == "december" or month == "january" or month == "february":
    print("You are a winter baby of two thousands.")
elif int(2000) <= int(year) and month == "march" or month == "april" or month == "may":
    print("You are a spring baby of two thousands.")
elif int(2000) <= int(year) and month == "june" or month == "july" or month == "august":
    print("You are a summer baby of two thousands.")
