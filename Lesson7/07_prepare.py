number = -1
while number < 0:
    number = int(input("\nPlease type a positive number: "))
    if number < 0:
        print("Sorry, that is a negative number. Please try again.")
        
print(f"The number is: {number}\n")

candy = "no"
while not candy == "yes":
    candy = input("May I have a piece of candy? ").lower()
    
print("\nThank you\n")