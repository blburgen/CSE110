# Milestone Requirements
# At the end of Lesson 03, to help make sure you are on track to finish the assignment, you need to complete the following:

# Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.
child_meal_price = float(input("What is the price of a child's meal? $"))
adult_meal_price = float(input("What is the price of an adult's meal? $"))

# Ask the user for the number of adults and children and store these values properly into variables as integers.
total_children = int(input("How many children are there? "))
total_adults = int(input("How many adults are there? "))

# Ask the user for the sales tax rate and store the value properly as a floating point number.
tax_rate = float(input("What is the sales tax rate(percentage)? "))

# Compute and display the subtotal (don't worry about rounding to two decimals at this point).
print(f"\nSubtotal: ${str(format(child_meal_price * total_children + adult_meal_price * total_adults,'.2f'))}")


# Final requirements
# At the end of Lesson 04, in addition to the milestone requirements above, you need to also complete the following:

# Compute and display the sales tax.


# Compute and display the total.


# Ask the user for the payment amount and store the value properly as a floating point number.


# Compute and display the change.


# Include a dollar sign ($) before each displayed value.

# Display each value to two decimals.

# Double check that the calculations are correct.

# Show creativity and exceed the core requirements by adding additional features.

# Use good style in your program, including variable names and whitespace.