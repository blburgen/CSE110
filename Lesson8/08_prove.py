import random

print("\nWelcome to the word guessing game!\n")

number = random.randint(1,10)
word = ""

match number:
    case 1:
        word = "hat"
    case 2:
        word = "mat"
    case 3:
        word = "mosiah"
    case 4:
        word = "nephi"
    case 5:
        word = "brady"
    case 6:
        word = "marie"
    case 7:
        word = "lizzy"
    case 8:
        word = "joe"
    case 9:
        word = "schwab"
    case _:
        word = "why"
        
guess_word = ""
guess_count = 0

print(f"\nYour hint is: ", end="")
for letter in word:
    print("_ ", end="")

while not guess_word == word:
    guess_word = input("\nWhat is your guess? ").lower()
    guess_count += 1
    
    if not guess_word == word:
        if len(guess_word) == len(word):
            print(f"\nYour hint is: ", end="")
            for i, letter in enumerate(guess_word):
                if letter == word[i]:
                    print(letter.upper(), end = " ")
                elif not word.find(letter) == -1:
                    print(letter.lower(), end = " ")
                else:
                    print("_", end=" ")
        
        else:
            print("Sorry, the guess must have the same number of letters as the secret word.")
    
    else:
        print("\nCongratulations! You guessed it!")

print(f"\nIt took you {guess_count} guesses.\n")

# Add the hints according to the rules above.

# Add a check to verify that the length of the 
# guess is the same as the length of the secret 
# word. If it is not, display a message. If they 
# are the same, then proceed to give the hint.

# Use a loop to generate the initial hint.

# Make sure to account for the following in your hints:

# Letters that are not present at all in the secret word (underscore _).

# Letters that are present in the secret word, but in a different spot (lowercase).

# Letters that are present in the secret word at that exact spot spot (uppercase).