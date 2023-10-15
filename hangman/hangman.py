import random
import hangman_art
import hangman_words

lives = 6

#word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(hangman_words.word_list)

#Test
print(f"To test, the word is {chosen_word}.")

display = []
for i in range(len(chosen_word)):
    display.append("_")
print(display)

while "_" in display:
    guess = input("Guess a letter that's in the word: ").lower()
    guessed_letter = False

    count = 0
    for letter in chosen_word:
        if letter == guess:
            display[count] = guess
            guessed_letter = True
            
        count += 1
        
    if guessed_letter == False:
        lives -= 1
        
    print(hangman_art.stages[lives])
            
    if lives == 0:
        print(f"Game Over. The word was {chosen_word}.")
        break;
    
    print(f"{' '.join(display)}")
    
if lives > 0:
    print("You win!")