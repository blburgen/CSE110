import math

square_length = float(input("\nWhat is the length of a side of the square(cm)? "))
print(f"{'The area of the square is: ':<30} {str(square_length**2)} square centimeters")
print(f"{'':<30} {str((square_length/100)**2)} square meters\n")

rectangle_length = float(input("What is the length of the rectangle(cm)? "))
rectangle_width = float(input("What is the width of the rectangle(cm)? "))
print(f"{'The area of the rectangle is:':<30} {str(rectangle_length * rectangle_width)} square centimeters")
print(f"{'':<30} {str(rectangle_length / 100 * rectangle_width / 100)} square meters\n")

circle_radius = float(input("What is the radius of the circle(cm)? "))
print(f"{'The area of the circle is:':<30} {str(math.pi * circle_radius**2)} square centimeters")
print(f"{'':<30} {str(math.pi * (circle_radius / 100)**2)} square meters\n")

side_length = float(input("Give a single length value(cm): "))
print(f"{'The area of the square is: ':<30} {str(side_length**2)} square centimeters")
print(f"{'':<30} {str((side_length/100)**2)} square meters\n")

print(f"{'The area of the circle is:':<30} {str(math.pi * side_length**2)} square centimeters")
print(f"{'radius ':<30} {str(math.pi * (side_length / 100)**2)} square meters\n")

print(f"{'The volume of the cube is: ':<30} {str(side_length**3)} cubed centimeters")
print(f"{'':<30} {str((side_length/100)**3)} cubed meters\n")

print(f"{'The volume of the sphere is:':<30} {str(4 / 3 * math.pi * side_length**3)} cubed centimeters")
print(f"{'':<30} {str(4 / 3 * math.pi * (side_length / 100)**3)} cubed meters\n")

# Prompt the user for a single length value, then compute and display the areas of a 
# square with that length of side, a circle with that radius, and then the volumes of 
# a cube with that side and a sphere with that radius, all from the same value from the user.