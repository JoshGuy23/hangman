import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#Test
print(f"To test, the word is {chosen_word}.")

guess = input("Guess a letter that's in the word: ").lower()

display = []
for i in range(0, len(chosen_word)):
    display.append("_")

count = 0
for letter in chosen_word:
    if letter == guess:
        print("Right")
        display[count] = guess
    else:
        print("Wrong")
    count += 1
    
print(display)