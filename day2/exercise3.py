# 💪This is a Difficult Challenge 💪

# Instructions
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:
# https://www.youtube.com/watch?v=xX96xng7sAE
# This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400

# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
# Example Input 1
# 2400
# Example Output 1
# Leap year.
# Example Input 2
# 1989
# Example Output 2
# Not leap year.

# Hint
# 1. Try to visualise the rules by creating a flow chart on www.draw.io
# 2. If you really get stuck, you can see the flow chart I created: https://bit.ly/36BjS2D


def input_validation(year):
    try:
        number = int(year)
        return True
    except ValueError:
        return False


def is_a_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (
        year % 4 == 0 and year % 100 == 0 and year % 400 == 0
    ):
        return True
    else:
        return False


def leap_year_calculation(year):
    is_valid = input_validation(year)
    if is_valid:
        year_number = int(year)
        is_leap = is_a_leap_year(year_number)
        if is_leap:
            return f"{year_number} is a Leap Year!"
        else:
            return f"{year_number} isn't a Leap Year!"
    else:
        return "Invalid Input"


calculating_year = leap_year_calculation(input("Input a Year:\n"))
print(calculating_year)
