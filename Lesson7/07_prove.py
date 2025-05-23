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

while not guess_word == word:
    guess_word = input("What is your guess? ").lower()
    guess_count += 1
    if not guess_word == word:
        print("Your guess was not correct.")
    else:
        print("\nCongratulations! You guessed it!")

print(f"\nIt took you {guess_count} guesses.\n")