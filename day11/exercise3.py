# Calculate Fibonacci Series
# Instructions
# Write a function called "calculate_fibonacci" that takes a number as input and calculates the Fibonacci series up to that number using global variables.
# Use a global list to store the series. Then, ask the user to enter a number, call the function with the input number, and print the Fibonacci series.
def calculate_fibonacci(n):
    a = 0
    b = 1

    for num in range(n):
        c = a+b
        a = b
        b = c
    return b
for numb in range(50):
    print(calculate_fibonacci(numb))