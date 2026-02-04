"""
PROJECT: Leap Year Checker

DESCRIPTION:
Write a program that returns True or False whether if a given year is a leap year. 
A normal year has 365 days, leap years have 366, with an extra day in February.

LOGIC:
- On every year that is divisible by 4 with no remainder 
- Except every year that is evenly divisible by 100 with no remainder  
- Unless the year is also divisible by 400 with no remainder   

EXAMPLES:
- Year 2000:  
    2000 ÷ 4 = 500 (Leap)  
    2000 ÷ 100 = 20 (Not Leap)  
    2000 ÷ 400 = 5 (Leap!)  
    Result: True

- Year 2100:  
    2100 ÷ 4 = 525 (Leap)  
    2100 ÷ 100 = 21 (Not Leap)  
    2100 ÷ 400 = 5.25 (Not Leap)  
    Result: False

WARNING: 
Your return should be a boolean (True/False). 
Do not use input(). Call the function with hard-coded values.
"""

def is_leap_year(year):
    # TODO: Write your logic here
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Testing the code:
print(is_leap_year(2400)) # Expected: True
print(is_leap_year(1989)) # Expected: False