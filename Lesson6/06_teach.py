age_first_rider = float(input("\nWhat is the age of the first rider in years? "))

if age_first_rider >= 12 and age_first_rider < 18:
    if input("Does the first rider have a golden passport (yes/no)? ").lower()[0] == "y":
        age_first_rider = 18
    
height_first_rider = float(input("What is the height of the first rider in inches? "))
second_rider = input("Is there a second rider (yes/no)? ").lower()
if second_rider[0] == "y":
    age_second_rider = float(input("What is the age of the second rider in years? "))
    
    if age_second_rider >= 12 and age_second_rider < 18:
        if input("Does the first rider have a golden passport (yes/no)? ").lower()[0] == "y":
            age_second_rider = 18
    
    height_second_rider = float(input("What is the height of the second rider in inches? "))
    
if second_rider[0] == "n":
    if height_first_rider < 36 or age_first_rider < 18 or height_first_rider < 62:
        print("\nSorry, you may not ride.\n")
    else:
        print("\nWelcome to the ride. Please be safe and have fun!\n")
        
elif second_rider[0] == "y":
    
    if (age_first_rider >= 12 and age_second_rider >= 12) and (height_first_rider >= 52 or height_second_rider >= 52):
        print("\nWelcome to the ride. Please be safe and have fun!\n")
    
    elif height_first_rider >= 36 and height_second_rider >= 36 and (age_first_rider >= 16 and age_second_rider >= 14 or age_first_rider >= 14 and age_second_rider >= 16):
        print("\nWelcome to the ride. Please be safe and have fun!\n")
        
    elif height_first_rider < 36 or height_second_rider < 36 or (age_first_rider < 18 and age_second_rider < 18):
        print("\nSorry, you may not ride.\n")
    
    else:
        print("\nWelcome to the ride. Please be safe and have fun!\n")

else:
    print("\nbad input\n")