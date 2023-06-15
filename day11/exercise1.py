# Count Vowels and Consonantsring.
# Instructions
# Use global variables to keep track of the counts.
# Then, ask the user to enter a string, call the function with the input string, and print the counts.
# Write a function called "count_vowels_consonants" that takes a string as input and counts the number of vowels and consonants
# in the string. Use global variables to keep track of the counts. Then, ask the user to enter a string,
# call the function with the input string, and print the counts.

# Hint:
# 1. Learn About Global and Local Variables
# 2. Use Functions for best practices
print("Bienvenidos al conteo de vocales y consonantes!")
letter = input("Ingrese su palabra o frase para hacer el conteo Vocales:\n")
def obtener_vocales(frase):
    vocales = "aeiouAEIOU"
    print("VOCALES")
    return set([palabra for palabra in frase if palabra in vocales])

print(obtener_vocales(letter))

letter1 = input("Ingrese su palabra o frase para hacer el conteo Consonantes:\n")
def obtener_vocales(frase):
    consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    print("CONSONANTES")
    return set([palabra for palabra in frase if palabra in consonantes])

print(obtener_vocales(letter1))
