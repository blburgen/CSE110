
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
    item = []
    item.append(input("What item would you like to add? ").title())
    item.append(float(input(f"What is the price of '{item[0]}'? ")))
    cart_items.append(item)
    print(f"'{item[0]}' has been added to the cart.")
    
def view_cart():
    print("The contents of the shopping cart are: ")
    for i in range(len(cart_items)):
        print(f"{i + 1}. {cart_items[i][0]:<20} - ${cart_items[i][1]:.2f}")
        
def remove_item():
    view_cart()
    item_to_remove = int(input("Which item would you like to remove? ")) - 1
    if item_to_remove < 0 or item_to_remove >= len(cart_items):
        print(f"{item_to_remove + 1} is not a option")
        return
    print(f"{cart_items[item_to_remove][0]} has been removed.")
    cart_items.pop(item_to_remove)
    
def compute_total():
    total = 0
    for item in cart_items:
        total += item[1]
    view_cart()
    print(f"The total price of the items in the shopping cart is ${total:.2f}")

while menu_choice != 5:
    menu_choice = menu()
    match menu_choice:
        case 1:
            add_item()
        case 2:
            view_cart()
        case 3:
            remove_item()
        case 4:
            compute_total()
    
print("\nThank you. Goodbye\n")