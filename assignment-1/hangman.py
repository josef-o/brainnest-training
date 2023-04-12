'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''
import random

WORDS = ["tree", "car", "queue", "equilibrium", "godzilla", "disestablishmentarianism", "kapow", "java", "foobar"]

def get_indices(letter: str, word: str) -> list[int]:
    """
    Returns the indices in word that match the given letter.
    """
    indices = []
    for i in range(len(word)):
        if word[i] == letter:
            indices.append(i)
    return indices

# pick a word to guess from a collection of predefined ones
word = random.choice(WORDS)
guess = ["_"] * len(word)
tries_left = 6
used_letters = set()
# to seed the input loop
user_letter = ""

while tries_left > 0:
    print(f"You have {tries_left} tries left.")
    print("Used letters:", " ".join(used_letters))
    print("Word:", " ".join(guess))
    print()
    
    while len(user_letter) != 1:
        print("Please enter a single letter: ", end="")
        user_letter = input().lower()
        # reject already guessed letters
        if user_letter in used_letters:
            print("You have already chosen that letter, pick a different one.")
            user_letter = ""
            
    used_letters.add(user_letter)
    guessed_indices = get_indices(user_letter, word)

    if not guessed_indices:
        tries_left -= 1
    for i in guessed_indices:
        guess[i] = user_letter
    
    # reset for next guess
    user_letter = ""
    
    if "".join(guess) == word:
        print(f"You guessed the word '{word}'!")
        break
        
if "".join(guess) != word:
    print("You didn't guess the word :/")
    print("It was:", word)
    
