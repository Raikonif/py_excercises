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


def count_vowels_consonants(string):
    string = string.replace(" ", "")
    total_vowels = 0
    total_consonants = 0
    for letter in string:
        if letter in "aeiou":
            total_vowels += 1
        else:
            total_consonants += 1

    print("Total vowels: ", total_vowels)
    print("Total consonants: ", total_consonants)


count_vowels_consonants("hola mundo")
