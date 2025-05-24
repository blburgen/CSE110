
number_list = []
print("Enter a list of numbers, type 0 when finished.")

new_number = 1
number_total = 0
number_count = 0
max_number = 0
min_number = 100000

while new_number != 0:
    new_number = int(input("Enter number: "))
    if new_number !=0:
        number_list.append(new_number)
        number_total += new_number
        number_count += 1
        if new_number > max_number:
            max_number = new_number
        if new_number < min_number and new_number > 0:
            min_number = new_number
            
print(f"The sum is: {number_total}")
print(f"The average is: {number_total / number_count}")
print(f"The largest number is: {max_number}")
print(f"The smallest positive number is: {min_number}")

number_list.sort()

for number in number_list:
    print(number)
        