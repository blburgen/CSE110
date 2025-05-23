grade_number = float(input("\nWhat is your grade percentage? "))

if grade_number >= 90:
    letter_grade = "A"
elif grade_number >= 80:
    letter_grade = "B"
elif grade_number >= 70:
    letter_grade = "C"
elif grade_number >= 60:
    letter_grade = "D"
else:
    letter_grade = "F" 

if grade_number > 95 or grade_number < 60:
    plus_minus = ""
elif grade_number%10 >= 7:
    plus_minus = "+"
elif grade_number%10 < 3:
    plus_minus = "-"
else:
    plus_minus = ""

print(f"\nYour grade is {letter_grade}{plus_minus}.\n")

if grade_number >= 70:
    print("Congratulation you passed!\n")
else:
    print("Sorry you did not pass.  Better luck next time.\n")