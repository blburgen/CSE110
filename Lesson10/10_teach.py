bank_accounts = []
current_balance = []

new_account = "yes"
total_amount = 0

print("Enter the names and balances of bank accounts (type: quit when done)")

while new_account[0] != "q":
    new_account = input("What is the name of this account? ").lower()
    if new_account[0] == "q":
        continue
    bank_accounts.append(new_account)
    current_balance.append(float(input("What is the balance? ")))
    
print("\nAccount Information:")

for i in range(len(bank_accounts)):
    print(f"{bank_accounts[i]:<20} - ${current_balance[i]:.2f}")
    total_amount += current_balance[i]
    
print(f"\nTotal: ${total_amount:.2f}")
print(f"Average: ${total_amount/len(bank_accounts):.2f}\n")