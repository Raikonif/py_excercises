# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# BMI = weight / height ** 2

# Warning you should convert the result to a whole number.

# Example Input
# weight = 80
# height = 1.75
# Example Output
# 80 ÷ (1.75 x 1.75) = 26.122448979591837
# 26

# Hint
# 1. Check the data type of the inputs.
# 2. Try to use the exponent operator in your code.
# 3. Remember PEMDAS.
# 4. Remember to convert your result to a whole number (int).

def validating_input(weight, height):
    if float(weight) > 0 and float(height) > 0 and weight.isdigit() and height.isdigit():
        return True
    else:
        return False
def bmi_calculator(weight, height):
    return float((weight / height) ** 2)

weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")

is_valid = validating_input(weight, height)
if is_valid:
    weight = float(weight)
    height = float(height)
    bmi = bmi_calculator(weight, height)
    print(bmi)
else:
    print("Invalid input")
