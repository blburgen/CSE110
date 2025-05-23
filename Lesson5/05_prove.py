# You need to have at least three levels of scenarios with possible choices.

# At least one of your scenarios must have more than two possible choices.

# In each prompt, write the choices in ALL CAPS, so that the user knows which 
# words are possible responses to choose.

# When checking the users responses, you should match on the keyword, regardless 
# of the uppercase/lowercase used in the response (e.g., "match", "MATCH", "Match" 
# should all work).

# Making different choices should take you to different scenarios. (You shouldn't 
# have the same result for different choices.)

# Choices should only work for the correct question.

# In other words, if one scenario resulted in choices of Run/Hide, but another 
# resulted in choices Follow/Look, you should not be able to respond with "Follow" 
# to the question that asked for Run/Hide.

# A good way to accomplish this is to have a series of nested if statements. 
# (That is, the print and then the next if statement will be within the body/block 
# of the first if statement.)

# For each question, you should provide an "else" clause to handle the case that the 
# user tries to type something other than the possible choices. It is up to you how 
# to handle this case.

print(f"\n{'':<35}Welcome to \"The Woods\" adventure game.\n")
print(f"{'':<20}At any time if you would like to quit the game you can type QUIT.\n")

play = True
win = False
died = False

while play:
    print("It is a wonderful day.  The sun is out and the birds are singing.  You see a wooded area off to you right.")
    level_one = input("\nWould you like to ENTER or WALK ON? ").lower()
    
    if level_one == "quit":
        play = False
    
    elif level_one == "enter":
        in_woods = True
        while in_woods:
            level_two = input("\nWhat would you like to do? ")
            
            if level_two == "quit":
                play = quit
                in_woods = False
                
            elif level_two == "win":
                print("\nYou overcame your fear of the woods.")
                play = False
                in_woods = False
                win = True
                
            elif level_two == "lie down and die":
                died = True
                play = False
                place = "in the woods"
                in_woods = False
                
            else:
                print(f"\n{level_two.title()} is not one of the options.  Please choose again.\n")
    
    elif level_one == "walk on":
        not_woods = True
        while not_woods:
            not_woods_two = input("\nWould you like to GO BACK? ").lower()
            
            if not_woods_two == "quit":
                play = False
                not_woods = False
            
            elif not_woods_two == "go back":
                not_woods = False
                
            elif not_woods_two == "lie down and die":
                died = True
                play = False
                place = "away from the woods"
                not_woods = False
                
            else:
                print(f"\n{not_woods_two.title()} is not one of the options.  Please choose again.\n")
                
    elif level_one == "lie down and die":
        died = True
        play = False
        place = "in front of the woods"
    
    else:
        print(f"\n{level_one.title()} is not one of the options.  Please choose again.\n")
    
if win:
    print("\nCongratulations you won!\n")
elif died:
    print(f"\nSorry you died {place}.  The worms and insects accept your sacrafice.\n")
else:
    print("\nYou coward! You ran from a good fight.\n")

# At the end of Lesson 05, to help make sure you are on track to finish the assignment, 
# you need to complete the following:

# The program is working for the first question and possible choices, and displays a 
# follow-up response to each choice (including an else condition).

# For the milestone, you do not need to implement any additional scenarios/questions, 
# you only need the first one.

# Create a design for your complete game.

# Prepare for the rest of your game by deciding on all the possible prompts, choices, 
# and responses that the user might see. You should design the complete game, including 
# else conditions. Then, to finish up the assignment for the next lesson, you'll just 
# need to code up all of these options.

# Feel free to write this design out on paper or in a document (Word, Google Docs, 
# Powerpoint, etc.), whatever is most convenient for you. You should write each 
# possible scenario along with its choices. Then, for each choice, write the 
# resulting scenario with its choices, etc.

# You are not required to submit this design to I-Learn, but you should complete 
# it as part of your Milestone to make sure you are prepared to finish the program.