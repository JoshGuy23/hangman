import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter that's in the word: ").lower()

if chosen_word.find(guess) != -1:
    print(f"Congratulations! The letter {guess} is in the word {chosen_word}!")
else:
    print(f"The letter {guess} is not in the word {chosen_word}.")