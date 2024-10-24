# -*- coding: utf-8 -*-
"""
EXERCISE5
DAYS OF THE MONTH
"""

month_days = {
    1: 31,  # January
    2: 28,  # February
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}
month = input("Enter a month number between 1 to 12: ").strip()
if month.isdigit():
    month = int(month)  
    if 1 <= month <= 12:
        days = month_days[month]
        print(f"Month {month} has {days} days.")
    else:
        print("Invalid month! Please enter a number between 1 and 12.")

#pulled all my hair out /joke