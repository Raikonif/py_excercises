print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# 1. create two choices left and right
# 2. if select left create the next choices wait or swim with different result
# 3. if the user select swim will be attacked by and angry trout. Game Over
# 4. if the user select wait will arrive to an Island and must select between 3 doors, red, yellow and blue
# 5. select the door that will give to the user the win and the others the loose. Game Over
# 6. if select right will fell into a hole and Game Over.


# Write your code below this line 👇
def tresaure_game(input_data):
    if input_data == "left":
        option = input("wanna 'swim' or 'wait'")
        if option == "swim":
            return "you has been attacked by and angry trout. Game Over"
        elif option == "wait":
            option2 = input(
                "are you arrived to an Island and must select between 3 doors, 'red', 'yellow' and 'blue'"
            )
            if option2 == "red":
                return "you win the prize of the treasure!"
            elif option2 == "yellow":
                return "you loose!. Game Over"
            elif option2 == "blue":
                return "you loose!. Game Over"
    else:
        return "you will fell into a hole. Game Over"


treasure = tresaure_game(input("Please Select 'left' or 'right' (typing the words)"))
print(treasure)
