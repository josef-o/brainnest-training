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
from random import randint

WORDS = ["tree", "car", "lordoftherings", "godzilla", "disestablishmentarianism", "kapow", "java", "foobar"]

def get_indices(letter: str, word: str):
    indices = []
    for i in range(len(word)):
        if word[i] == letter:
            indices.append(i)
    return indices


word = WORDS[randint(0, len(WORDS))]

guess = ["_"] * len(word)

tries_left = 6
used_letters = set()
    
while tries_left > 0:
    print("You have", tries_left, "tries left.")
    print("Used letters:", " ".join(used_letters))
    print("Word:", " ".join(guess))
    print()
    
    user_letter = input("Guess a letter: ")
    used_letters.add(user_letter)
    guessed = get_indices(user_letter, word)
    if not guessed:
        tries_left -= 1
        continue
        
    for i in guessed:
        guess[i] = user_letter
    
    if "".join(guess) == word:
        print("You guessed the word " + word + "!")
        break
        
if "".join(guess) != word:
    print("You didn't guess the word :/")
    print("It was:", word)
    