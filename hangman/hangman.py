import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#Test
print(f"To test, the word is {chosen_word}.")

guess = input("Guess a letter that's in the word: ").lower()

display = []
for i in range(1, len(chosen_word)):
    display.append("_")

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")