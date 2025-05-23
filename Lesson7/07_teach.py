import random

play = "yes"

while play[0] == "y":
    number = random.randint(1,100)
    print("\nTry to guess the magic number")

    number_guess = -1
    guess_count = 0

    while not number_guess == number:
        
        number_guess = int(input("What is your guess? "))
        guess_count += 1
        
        if number > number_guess:
            print("Higher")
        
        elif number == number_guess:
            print(f"You guessed it!  It took you {guess_count} guesses.\n")
        
        else:
            print("Lower")
            
    play = input("Would you like to play again (yes/no)? ").lower()

print("\nThank you for playing\n")