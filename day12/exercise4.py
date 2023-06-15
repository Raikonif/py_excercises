import random
# Number Guessing Game
# Instructions
# Write a program that generates a random number between 1 and 100 and asks the user to guess the number.
# Provide feedback if the guess is too high or too low. Use a while loop and a global variable to keep track of the number of guesses.
intentos = 0
numero_min = 1
numero_max = 100

name = input("Ingrese nombre jugador:\n")

rdm = random.randint(numero_min, numero_max)
print("Empecemos", name, ".Estoy pensando en un numero del",str(numero_min), "al", str(numero_max))

while intentos <5:
    print("Adivina")
    number = int(input("El numero:\n"))

    intentos = intentos +1

    if number < rdm:
        print("Numero muy bajo")
    elif number > rdm:
        print("Numero muy alto")
    elif number == rdm:
        break
if number == rdm:
    intentos = str(intentos)
    print("GANASTE!!!", name, "Adivinaste en:", intentos, "intentos")