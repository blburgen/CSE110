item_list = []

print("\nPlease enter the items of the shopping list (type: quit to finish):")

item = " "

while item[0] != "Q":
    item = input("Item: ").title()
    if item[0] != "Q":
        item_list.append(item)
        
print("\nThe shopping list is:")
for item in item_list:
    print(item)

print("\nThe shopping list with indexes is:")
for i in range(len(item_list)):
    print(f"{i}. {item_list[i]}")
    
change_item = int(input("\nWhich item would you like to change? "))
item = input("What is the new item? ").title()
item_list.pop(change_item)
item_list.insert(change_item, item)

print("\nThe shopping list with indexes is:")
for i in range(len(item_list)):
    print(f"{i}. {item_list[i]}")