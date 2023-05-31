rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Create a the game rock, paper, scissors
# Write your code below this line 👇
print("HI!, Empecemos el juego")
option= ["piedra", "papel", "tijera"]
while True:
    player = input("PLayer Elije: piedra, papel, tijera: ").lower()
    if player not in option:
        print("Movimiento no valido")
    pc = random.choice(option)
    print(f"La PC ha seleccionado {pc}")
    if player == pc:
        print(f"Empate!, ambos eligeron {player}")
    elif player == "piedra" and pc == "tijeras":
        print("Ganaste Player!")
    elif player == "tijeras" and pc == "papel":
        print("Ganaste Player!")
    elif player == "papel" and pc == "piedra":
        print("Ganaste Player!!")
    else:
        print(f"Game Over, P E R D I S TE {player} pierde en contra {pc}")
