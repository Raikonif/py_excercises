# Instructions
# Write a program that works out whether if a given number is an odd or even number.

# Even numbers can be divided by 2 with no remainder.
# e.g. 86 is even because 86 ÷ 2 = 43

# 43 does not have any decimal places. Therefore the division is clean.
# e.g. 59 is odd because 59 ÷ 2 = 29.5

# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
# e.g.
# 6 ÷ 2 = 3 with no remainder.
# therefore: 6 % 2 = 0
# 5 ÷ 2 = 2 x 2 + 1, remainder is 1.
# therefore: 5 % 2 = 1
# 14 ÷ 4 = 3 x 4 + 2, remainder is 2.
# therefore: 14 % 4 = 2
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input 1
# 43
# Example Output 1
# This is an odd number.
# Example Input 2
# 94
# Example Output 2
# This is an even number.

# Hint
# 1. All even numbers can be divided by 2 with 0 remainder.
# 2. Try some using the modulo with some odd numbers e.g.
# 3 % 2
# 5 % 2
# 7 % 2
# 3. Then try using the modulo with some even numbers e.g.
# 4 % 2
# 6 % 2
# 8 % 2
# See what's in common each time.


def input_validation(number):
    if number.isdigit() and float(number).is_integer():
        return True
    else:
        return False


def is_even_number(number):
    is_valid_number = input_validation(number)
    if is_valid_number:
        if int(number) % 2 == 0:
            return "Is Even Number"
        else:
            return "Is Odd Number"
    else:
        return "Invalid Input"


number_type = is_even_number(input("Write a number to know if it is even or odd\n"))
print(number_type)
