import datetime

"""
Documentation for determining lear found on:
https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
A leap year is evenly divisible by 4, 100, and 400
"""
def is_leap_year(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

"""
Algorithm for DOTY was found on page 8 of:
Practical Astronomy with your Calculator or Spreadsheet, 4th Edition by Peter Duffett-Smith, Jonathan Zwart
"""
def get_doty():
    # Get the Date
    current_time = datetime.datetime.now()
    month = int(current_time.strftime("%m"))
    day = int(current_time.strftime("%d"))
    year = int(current_time.strftime("%Y"))

    if month > 2:
        day_of_the_year = int((month + 1) * 30.6)
        if is_leap_year(year):
            day_of_the_year = (day_of_the_year - 62) + day
        else:
            day_of_the_year = (day_of_the_year - 63) + day
    else:
        day_of_the_year = month - 1
        if is_leap_year(year):
            day_of_the_year = day_of_the_year * 62
        else:
            day_of_the_year = day_of_the_year * 63
        day_of_the_year = (int(day_of_the_year / 2)) + day

    return day_of_the_year
