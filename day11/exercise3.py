# Calculate Fibonacci Series
# Instructions
# Write a function called "calculate_fibonacci" that takes a number as input and calculates the Fibonacci series up to that number using global variables.
# Use a global list to store the series. Then, ask the user to enter a number, call the function with the input number, and print the Fibonacci series.
x = 0
y= 1
z= 0
while True:
    number = int(input("Ingrese un numero mayor a 1:\n"))
    if number > 1:
        break
    print("1", end = " ")
    for num in range(0,n):
        z = x+y
        print(f"{z}", end = " ")
        x = y
        y = z
    print("")