# Download the dataset
with open("life-expectancy.csv") as life_expectancy:
# Load the dataset in your Python program
    life_list = []
    
    min_life = 110.0
    min_location = ""
    min_year = "0"
    
    max_life = 0.0
    max_location = ""
    max_year = "0"
    
    user_min_life = 110.0
    user_min_location = ""
    
    user_max_life = 0.0
    user_max_location = ""
    
    count = 0
    total = 0.0
    
    user_year = int(input("\nEnter the year of interest: "))
    
    user_country = input("Enter a country of interest: ")
    user_min = 110
    user_min_year = 0
    user_max = 0
    user_max_year = 0

    for line in life_expectancy:
        new_line = line.strip().split(",")
        if new_line[3][0] == "L":
            continue
        life_rate = float(new_line[3])
        if life_rate > max_life:
            max_life = life_rate
            max_location = new_line[0]
            max_year = int(new_line[2])
        if life_rate < min_life:
            min_life = life_rate
            min_location = new_line[0]
            min_year = int(new_line[2])
        if int(new_line[2]) == user_year:
            count += 1
            total += life_rate
            if life_rate > user_max_life:
                user_max_life = life_rate
                user_max_location = new_line[0]
            if life_rate < user_min_life:
                user_min_life = life_rate
                user_min_location = new_line[0]
        if new_line[0].lower() == user_country.lower():
            if life_rate > user_max:
                user_max = life_rate
                user_max_year = int(new_line[2])
            if life_rate < user_min:
                user_min = life_rate
                user_min_year = int(new_line[2])
            
            
    # Iterate through the data line by line

    # Split each line into parts
    print(f"\nThe overall max life expectancy is: {max_life} from {max_location} in {max_year}")
    print(f"The overall min life expectancy is: {min_life} from {min_location} in {min_year}")

    print(f"\nFor the year {user_year}:")
    print(f"The average life expectancy across all countries was {total/count:.2f}")
    print(f"The max life expectancy was in {user_max_location} with {user_max_life}")
    print(f"The min life expectancy was in {user_min_location} with {user_min_life}\n")

    print(f"For {user_country.title()}:")
    print(f"The max life expectancy was {user_max} in year {user_max_year}")
    print(f"The min life expectancy was {user_min} in year {user_min_year}\n")
    
    
    # Find the lowest value for life expectancy and the 
    # highest value for life expectancy in the dataset. 
    # (Note that at this point, you just need the value for 
    # this, not the year and the country for that value.)