
print("Welcome to the Shopping Cart Program!")

menu_choice = 0
cart_items = []

def menu():
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    number = int(input("Please enter an action: "))
    return number

def add_item():
    item = input("What item would you like to add? ")
    cart_items.append(item)
    print(f"'{item}' has been added to the cart.")
    
def view_cart():
    print("The contents of the shopping cart are: ")
    for item in cart_items:
        print(item)

while menu_choice != 5:
    menu_choice = menu()
    match menu_choice:
        case 1:
            add_item()
        case 2:
            view_cart()
    
print("\nThank you. Goodbye\n")