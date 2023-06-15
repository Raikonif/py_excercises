# Sum of Digits
# Instructions
# Write a program that asks the user to enter a positive integer and then calculates the sum of its digits using a while loop.
# Use a global variable to keep track of the current digit.
n = int(input("Ingresa tu numero:\n"))
suma = 0
while n > 0:
    suma = suma + (n % 10)
    n = n // 10
print("La suma de los digitos es:", suma)