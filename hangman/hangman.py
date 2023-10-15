import random
import hangman_art
import hangman_words

lives = 6

#word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)

#Test
print(f"To test, the word is {chosen_word}.")

display = []
for i in range(len(chosen_word)):
    display.append("_")
print(display)

guessed_letters = []
wrong = []
while "_" in display:
    guess = input("Guess a letter that's in the word: ").lower()
    guessed_letter = False
    
    if guess in guessed_letters:
        print(f"You already guessed {guess}. Try again.")
        continue
    else:
        guessed_letters.append(guess)

    count = 0
    for letter in chosen_word:
        if letter == guess:
            display[count] = guess
            guessed_letter = True
            
        count += 1
        
    if guessed_letter == False:
        wrong.append(guess)
        print(f"Wrong: {wrong}")
        lives -= 1
        
    print(hangman_art.stages[lives])
            
    if lives == 0:
        print(f"Game Over. The word was {chosen_word}.")
        break;
    
    print(f"{' '.join(display)}")
    
if lives > 0:
    print("You win!")