first_number = int(input("\nEnter an integer: "))
second_number = int(input("Enter another integer: "))

if first_number > second_number:
    print("The first number is greater")
else:
    print("The first number is not greater")
    
if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")
    
if first_number < second_number:
    print("The second number is greater\n")
else:
    print("The second number is not greater\n")
    
my_favorite_animal = "dog"
favorite_animal = input("What is your favorite animal? ").lower()

if my_favorite_animal == favorite_animal:
    print("That's my favorite animal too!\n")
else:
    print("That one is not my favorite.\n")