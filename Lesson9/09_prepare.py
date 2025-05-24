friend_list = []

new_friend = ""

while new_friend != "end":
    new_friend = input("Type the name of a friend: ")
    if new_friend != "end":
        friend_list.append(new_friend)
 
print(f"\nYour friends are:")       
for friend in friend_list:
    print(friend)