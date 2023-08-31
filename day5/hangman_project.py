# Step 1
from random import choice

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# TODO 4 - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'.
# TODO 5 - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# TODO 6 - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".


def chossen_word():
    word_list = ["aardvark", "baboon", "camel"]
    return choice(word_list)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    word_to_guess = chossen_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman")
    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            guessed_letters.append(guess)
            if guess not in word_to_guess:
                attempts -= 1
                print("Incorrect guess. Attempst Left: ", attempts)
            if "_" not in display_word(word_to_guess, guessed_letters):
                print("\nCongratulations! You Guessed the word: ", word_to_guess)
                break
            if attempts == 0:
                print("\nGame Over. The word was: ", word_to_guess)
                break


hangman()
