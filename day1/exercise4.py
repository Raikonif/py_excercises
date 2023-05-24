# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# Hint
# 1. There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# 2. Try copying the example output into your code and replacing the relevant parts so that the sentence is formated the same way.\


def years_left(age):
    years = 90 - int(age)
    months = years * 12
    weeks = years * 52
    days = years * 365
    return f"You have {days} days, {weeks} weeks, and {months} months left."


def validating_age(age):
    if age.isdigit() and int(age) > 0:
        return True
    else:
        return False


input_age = input("What is your current age? ")
is_valid = validating_age(input_age)
if is_valid:
    life_left = years_left(input_age)
    print(life_left)
else:
    print("Invalid input")
