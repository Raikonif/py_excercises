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

from random import randint

game_images = [rock, paper, scissors]
game_options = ["rock", "paper", "scissors"]
game_matches = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

player_input = int(
    input(
        """
select your choice:
1. Rock
2. Paper
3. Scissors
"""
    )
)
computer_input = randint(1, 3)
g
player_choice = game_options[player_input - 1]
computer_choice = game_options[computer_input - 1]

player_image = game_images[player_input - 1]
computer_image = game_images[computer_input - 1]

print(player_image, computer_image)

if player_choice == computer_choice:
    print("Draw")
elif game_matches[player_choice] == computer_choice:
    print("You Win!")
else:
    print("You Loose!")
