# Import the random module, as well has hangman_art.py and hangman_words.py for the ASCII art and word selection, respectively.
import random
import hangman_art
import hangman_words

# The number of lives the player has.
lives = 6

#word_list = ["aardvark", "baboon", "camel"]

# Randomly select a word for the player to guess.
chosen_word = random.choice(hangman_words.word_list)

# Print the logo.
print(hangman_art.logo)

#Test
#print(f"To test, the word is {chosen_word}.")

# Create a list of blanks that represents the word that was selected for the game and display it.
display = []
for i in range(len(chosen_word)):
    display.append("_")
print(display)

# Create lists for guessed letters and wrong answers.
guessed_list = []
wrong = []

# The game will continue until the player either runs out of lives or guesses all letters.
while "_" in display:
    # Get the user to input a letter to guess. This letter is always lowercase.
    guess = input("Guess a letter that's in the word: ").lower()
    guessed_letter = False
    
    # If the user guesses a letter they already guessed, they receive an error message and the game continues.
    # Otherwise, add the new guess to the list of guesses made
    if guess in guessed_list:
        print(f"You already guessed {guess}. Try again.")
        continue
    else:
        guessed_list.append(guess)

    # Counter used to keep track of the position of the word.
    count = 0
    # For every letter in the word, if it matches the user's guess, add it to the incomplete word in its respective position.
    # After every loop, increment the current position in the word.
    for letter in chosen_word:
        if letter == guess:
            display[count] = guess
            guessed_letter = True
            
        count += 1
     
    # If there was no match at all, add the wrong guess to a list of wrong guesses, then print it, then remove a life.
    if guessed_letter == False:
        wrong.append(guess)
        print(f"Wrong: {wrong}")
        lives -= 1
    
    # Print the ASCII art for the current amount of lives.
    print(hangman_art.stages[lives])
    
    # If the player loses all of their lives, display a game over message and the word they were trying to guess.
    # Then, exit the loop.
    if lives == 0:
        print(f"Game Over. The word was {chosen_word}.")
        break;
    
    # Display the player's progress.
    print(f"{' '.join(display)}")

# If the player guessed the word without losing all their lives, display a congratulatory message.
if lives > 0:
    print("You win!")