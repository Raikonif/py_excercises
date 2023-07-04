# 💪 This is a Difficult Challenge 💪

# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."
# e.g.
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5

# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3

# Love Score = 53
# Print: "Your score is 53."

# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Example Output 1
# Your score is 42, you are alright together.
# Example Input 2
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"
# Example Output 2
# Your score is 73.

# The testing code will check for print output that is formatted like one of the lines below:
# "Your score is 47, you are alright together."
# "Your score is 125, you go together like coke and mentos."
# "Your score is 54."

# Score Comparison
# Not sure you're getting the correct score for the exercise? Use this table to check your code's score against mine.

# Name 1	               Name 2	           Score
# Catherine Zeta-Jones     Michael Douglas     99
# Brad Pitt	               Jennifer Aniston	   73
# Prince William	       Kate Middleton	   67
# Angela Yu	               Jack Bauer	       53
# Kanye West	           Kim Kardashian	   42
# Beyonce	               Jay-Z	           23
# John Lennon	           Yoko Ono	           18

# Hint
# 1. The lower() function changes all the letters in a string to lowercase.
# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
# 2. The count() function will give you the number of times a letter occurs in a string.
# https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string

TRUE = "true"
LOVE = "love"


def counting_points(name):
    total_true = 0
    total_love = 0
    total_true += name.count("t")
    total_true += name.count("r")
    total_true += name.count("u")
    total_true += name.count("e")
    total_love += name.count("l")
    total_love += name.count("o")
    total_love += name.count("v")
    total_love += name.count("e")
    return total_true, total_love


def true_calculator(name1, name2):
    name1_modified = name1.lower()
    name2_modified = name2.lower()
    name1_true, name1_love = counting_points(name1_modified)
    name2_true, name2_love = counting_points(name2_modified)
    return str((name1_true + name2_true)) + str((name1_love + name2_love))


total = true_calculator("Nandy", "Diego")
print("total compatibility", total)
