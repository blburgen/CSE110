# Requirement
# create a mad lib using the following:

# The other day, I was really in trouble. It all started when I saw a very
# [adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
# I could think to do was to [verb] over and over. Miraculously,
# that caused it to stop, but not before it tried to [verb]
# right in front of my family.



import random
play = "Yes"

def lib_one():
    print("\nPlease enter the following:\n")
    noun_one = input("Name: ").title()
    adjective_one = input("adjective: ")
    animal_one = input("animal: ")
    verb_one = input("verb: ")
    exclamation_one = input("exclamation: ").title()
    verb_two = input("verb: ")
    verb_three = input("verb: ")

    print("\nYour story is:\n")

    print(f"The other day, {noun_one} was really in trouble. It all started when {noun_one} saw a very")
    print(f"{adjective_one} {animal_one} {verb_one} down the hallway. \"{exclamation_one}!\" {noun_one} yelled. But all")
    print(f"{noun_one} could think to do was to {verb_two} over and over. Miraculously,")
    print(f"that caused it to stop, but not before it tried to {verb_three}")
    print(f"right in front of {noun_one}'s family.\n")
    
def lib_two():
    print("\nPlease enter the following:\n")
    verb_one = input("verb: ")
    adjective_one = input("adjective: ")
    adjective_two = input("adjective: ")
    noun_one = input("noun: ")
    noun_one_article = "a"
    if noun_one[0] == "a" or noun_one[0] == "e" or noun_one[0] == "i" or noun_one[0] == "o" or noun_one[0] == "u":
        noun_one_article = "an" 
    noun_two = input("noun: ")
    noun_two_article = "a"
    if noun_two[0] == "a" or noun_two[0] == "e" or noun_two[0] == "i" or noun_two[0] == "o" or noun_two[0] == "u":
        noun_two_article = "an"
    direction_one = input("direction: ")
    
    print("\nYour story is:\n")
    
    print(f"A vacation is when you take a {verb_one} to some {adjective_one} place")
    print(f"with your {adjective_two} family.  You go to some place")
    print(f"that is near {noun_one_article} {noun_one} or {direction_one} on {noun_two_article} {noun_two}.\n")
    
def lib_three():
    print("\nPlease enter the following:\n")
    location_one = input("location: ")
    title_one = input("title of a person: ").title()
    fealing_one = input("fealing: ")
    pronoun_one = input("pronoun: ").title()
    noun_one = input("noun: ")
    noun_one_article = "a"
    if noun_one[0] == "a" or noun_one[0] == "e" or noun_one[0] == "i" or noun_one[0] == "o" or noun_one[0] == "u":
        noun_one_article = "an"
        
    print("\nYour story is:\n")
    
    print(f"One day, in a {location_one} far way.  There was a {title_one}")
    print(f"that was so {fealing_one}.  {pronoun_one} did not have {noun_one_article} {noun_one} in")
    print(f"the whole world.\n")

while play[0] == "Y":
    num = random.randint(1,3)

    match num:
        case 1:
            lib_one()
        case 2:
            lib_two()
        case 3:
            lib_three()
    
    play = input("Would you like to play again(yes/no):").strip().title()
    if play == "":
        play = "N"
        

    
