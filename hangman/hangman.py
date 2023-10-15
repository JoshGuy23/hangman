import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter that's in the word: ").lower()