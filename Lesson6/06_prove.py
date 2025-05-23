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
print(f"{'':<20}At any time if you would like to quit the game you can type QUIT.")

play = True
win = False
died = False

while play:
    print("\nIt is a wonderful day.  The sun is out and the birds are singing.  You see a wooded area off to you right.")
    level_one = input("\nWould you like to ENTER or WALK ON or QUIT? ").lower()
    
    if level_one == "quit":
        win = False
        play = False
    
    elif level_one == "enter":
        in_woods = True
        while in_woods:
            
            print("\nIt gets really dark in the woods, but you can see two objects in front of you.  A large matchstick and a flashlight are on the path.")
            level_two = input("\nWould you like to GO Back or USE THE MATCH or USE THE FLASHLIGHT or GO ON IN THE DARK? ").lower()
            
            if level_two == "quit":
                win = False
                play = False
                in_woods = False
                
            elif level_two == "go back":
                in_woods = False
                 
            elif level_two == "use the match":
                print("\nThe woods lights up for a brief second and you see a bear.  He looks hungry and you are frozen in fear.")
                place = "while being eaten by a bear"
                in_woods = False
                died = True
                play = False
                if win:
                    print("\nThe kind fairy saves you from the bear.")
            
            elif level_two == "use the flashlight":
                
                print("\nThe flashlight turns on and lights the path before you.  In the path in front of you is two different paths.")
                level_three = input("\nAre you going RIGHT or LEFT? ").lower()
                
                if level_three == "right":
                    print("\nYou found a hoard of gold.")
                    win = True
                    in_woods = False
                    play = False
                    
                elif level_three == "left":
                    died = True
                    place = "in the woods, never to be hear of again"
                    in_woods = False
                    play = False
            
            elif level_two == "go on in the dark":
                print("\nYou stumble around in the dark for a little while until you fall of a cliff.")
                place = "going off a cliff"
                died = True
                play = False
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
                print(f"\n{level_two.title()} is not one of the options.  Please choose again.")
    
    elif level_one == "walk on":
        not_woods = True
        while not_woods:
            print("\nYou found a creepy old house that is blocking the path.")
            not_woods_two = input("\nWould you like to GO BACK or GO INTO HOUSE or SING A SONG? ").lower()
            
            if not_woods_two == "quit":
                win = False
                play = False
                not_woods = False
                
            elif not_woods_two == "go into house":
                
                in_house = True
                while in_house:
                    
                    print("\nIn the house you see a old naked hag.  She is upset that you walk in on her.")
                    last_decision = input("\nWould you like to STAND AND WATCH or LIE DOWN AND DIE or RUN? ").lower()
                    
                    if last_decision == "stand and watch":
                        in_house = False
                        not_woods = False
                        died = True
                        place = "while watching a old naked hag"
                        play = False
                        print("\nThe old hag uses her laser eyes to cut you in two. She then laughs evilly.")
                        if win:
                            print("\nThe fairy's magic saved you from dying.")
                    
                    elif last_decision == "quit":
                        win = False
                        in_house = False
                        not_woods = False
                        play = False
                        
                    elif last_decision == "lie down and die":
                        in_house = False
                        not_woods = False
                        died = True
                        place = "in creepy old house"
                        play = False
                        if win:
                            print("\nThe fairy's magic saved you from dying.")
                        
                    elif last_decision == "run":
                        print("\nYou ran away as fast as you could from that old bag.")
                        in_house = False
                        not_woods = False
                        
                    else:
                        print(f"\n{last_decision.title()} is not one of the options.  Please choose again.")
                    
            elif not_woods_two == "sing a song":
                
                song = True
                while song:
                    
                    print("\nA fairy appears in front of you.  She compliments you on your beautiful voice.")
                    fairy_question = input("\nShe asks you a \"Do you think I am beautiful (yes/no)?\" ").lower()
                    
                    if fairy_question[0] == "y":
                        print("\nShe thanks you for your kindness and taps you with her wand.  She then disappears.")
                        win = True
                        song = False
                    
                    elif fairy_question == "quit":
                        win = False
                        song = False
                        not_woods = False
                        play = False
                    
                    elif fairy_question[0] == "n":
                        win = False
                        died = True
                        song = False
                        not_woods = False
                        play = False
                        place = "while insulting a fairy"
                        
                    else:
                        print(f"\n{fairy_question.title()} is not one of the options.  Please choose again.")
            
            elif not_woods_two == "go back":
                not_woods = False
                
            elif not_woods_two == "lie down and die":
                died = True
                play = False
                place = "away from the woods"
                not_woods = False
                
            else:
                print(f"\n{not_woods_two.title()} is not one of the options.  Please choose again.")
                
    elif level_one == "lie down and die":
        died = True
        play = False
        place = "in front of the woods"
    
    else:
        print(f"\n{level_one.title()} is not one of the options.  Please choose again.")
    
if win:
    print("\nCongratulations you won!\n")
elif died:
    print(f"\nSorry you died {place}.  The worms and insects accept your sacrifice.\n")
else:
    print("\nYou coward! You ran from a good fight.\n")
