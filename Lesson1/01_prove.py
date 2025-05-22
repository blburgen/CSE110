"""
    This is the prove assignment for lesson 1.
    The requirements for this assignment are to ask for a users color and then print it out.
    
    In this assingment I have added the following:
    1 - a greeting message
    2 - two extra question (name and favorite food)
    3 - made the question unique
    4 - printed out the variable on the same line as the output statement
"""

print("\nHello\nI am going to ask you a few questions.  Please answer as truthfully as you can.\n")

user_name = input("What is your name: ")
favorite_color = input("What color would you love to be surround by: ")
favorite_food = input("If you could only eat one thing for the rest of you life, what would it be: ")

print(f"\nHello, {user_name}!")
print(f"Your favorite color is {favorite_color}.")
print(f"Your favorite food is {favorite_food}.\n")