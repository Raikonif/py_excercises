# create a calculator that can +, -, *, / between 2 or more numbers
# make a variable validation function to know if the input is a valid number

# e.g:

# operation *
# inputs 1 , 4, 5
# output 20

# operation -
# inputs 2, 4, 6, 2
# output -10

# operation /
# inputs 2,2
# output 1
from itertools import product

input_operation = input("Enter the operation: ")
input_numbers = input("Enter the numbers: ").split(" ")


def validation_input(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def calculator(operation, numbers):
    list_numbers = list(numbers)
    mapped_numbers = map(int, list_numbers)
    print(mapped_numbers)
    if operation == "+":
        result = sum(mapped_numbers)
        return result
    elif operation == "-":
        result = 0
        for number in mapped_numbers:
            result -= number
        return result
    elif operation == "*":
        result = 1
        for number in mapped_numbers:
            result *= number
        return result
    elif operation == "/":
        result = 1
        for number in mapped_numbers:
            result /= number
        return result


print(calculator(input_operation, input_numbers))
