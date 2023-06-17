# Palindrome Checker
# Instructions
# Write a program that prompts the user to enter a word and checks if it is a palindrome.
# A palindrome is a word that is the same when read forwards and backwards.

# Hints:
# Use string slicing to reverse the word and check if it matches the original word.
# Define a function called is_palindrome(word) that takes a word as input and returns True if it is a palindrome, and False otherwise.
# Use a while loop to continue asking the user for a word until a palindrome is entered.
intentos = 0
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

while intentos < 4:
    usuario = input("Ingrese palabra u oracion:\n")
    intentos = intentos+1

    if usuario == True:
        print("Ingrese siguiente palabra u oracion:\n")
    elif usuario == False:
        print("Ingrese siguiente palabra u oracion:\n ")

print(is_palindrome(usuario))


