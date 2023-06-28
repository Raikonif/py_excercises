# Number Guessing Game Objectives:

# Include an ASCII art logo. http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
intentos = 0
number = 50

print("Bienvenido al juego Adivina Adivinador")
name = input("Ingrese nombre jugador:\n")
modo = input("Ingrese modo de Juego: 1=Easy 2=Hard:\n")
print("Empecemos", name, ".Estoy pensando en un numero del 1 al 100")
if modo == "1":
    while intentos <5:
        print("Adivina")
        player = int(input("El numero:\n"))

        intentos = intentos +1

        if player < number:
            print("Numero muy bajo")
        elif player > number:
            print("Numero muy alto")
        elif player == number:
            break
    if player == number:
        intentos = str(intentos)
        print("GANASTE!!!", name, "Adivinaste en:", intentos, "intentos")
elif modo == "2":
    while intentos <3:
        print("Adivina")
        player = int(input("El numero:\n"))

        intentos = intentos +1

        if player < number:
            print("Numero muy bajo")
        elif player > number:
            print("Numero muy alto")
        elif player == number:
            break
    if player == number:
        intentos = str(intentos)
        print("GANASTE!!!", name, "Adivinaste en:", intentos, "intentos")

