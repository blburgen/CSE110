import math

def compute_area_square(length):
    return compute_area_rectangle(length, length)

def compute_area_rectangle(length, width):
    return length * width
    
def compute_area_circle(radius):
    return math.pi * radius**2
    
choice = -1
    
while choice != 0:
    print("Choose one of the following to calculate the area of (0-3):")
    print("0. Quit")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    choice = int(input("What to do want to do? "))
    
    if choice == 1:
        square_length = float(input("\nWhat is the length of a side of the square(cm)? "))
        square_area = compute_area_square(square_length)

        print(f"{'The area of the square is: ':<30} {square_area} square centimeters")
        print(f"{'':<30} {square_area/(100**2)} square meters\n")

    elif choice == 2:
        rectangle_length = float(input("What is the length of the rectangle(cm)? "))
        rectangle_width = float(input("What is the width of the rectangle(cm)? "))
        rectangle_area = compute_area_rectangle(rectangle_length, rectangle_width)

        print(f"{'The area of the rectangle is:':<30} {rectangle_area} square centimeters")
        print(f"{'':<30} {rectangle_area / 10000} square meters\n")

    elif choice == 3:
        circle_radius = float(input("What is the radius of the circle(cm)? "))
        circle_area = compute_area_circle(circle_radius)

        print(f"{'The area of the circle is:':<30} {circle_area} square centimeters")
        print(f"{'':<30} {circle_area / 10000} square meters\n")
        
    elif choice == 0:
        print("\nMoving on.\n")
        
    else:
        print("\nInvalid choice\n")

side_length = float(input("Give a single length value(cm): "))
print(f"{'The area of the square is: ':<30} {str(side_length**2)} square centimeters")
print(f"{'':<30} {str((side_length/100)**2)} square meters\n")

print(f"{'The area of the circle is:':<30} {str(math.pi * side_length**2)} square centimeters")
print(f"{'radius ':<30} {str(math.pi * (side_length / 100)**2)} square meters\n")

print(f"{'The volume of the cube is: ':<30} {str(side_length**3)} cubed centimeters")
print(f"{'':<30} {str((side_length/100)**3)} cubed meters\n")

print(f"{'The volume of the sphere is:':<30} {str(4 / 3 * math.pi * side_length**3)} cubed centimeters")
print(f"{'':<30} {str(4 / 3 * math.pi * (side_length / 100)**3)} cubed meters\n")