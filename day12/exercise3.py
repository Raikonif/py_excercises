# Factorial Calculator
# Instructions
# Write a program that asks the user to enter a positive integer and then calculates its factorial
# using a while loop. Use a global variable to keep track of the current multiplication factor.
print("Hola!")
number = int(input("Ingrese un numero"))
if number >= 0:
    x = 1
    factorial = 1
    while x <= number:
        factorial = factorial * x
        x += 1
    print("El factorial de", number, "es:", factorial, "positivo")
else:
    print("No se puede calcular")
