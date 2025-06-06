# Create a string variable to hold the word "Commitment".
word = "Commitment".lower()
input_letter = input("\nWhat is your favorite letter? ").lower()
# Write code that loops through the word letter by letter. 
# If the letter is "m", print it as a capital letter. If 
# the letter is anything else, print it out as a lowercase letter.
for letter in word:
    if letter == input_letter:
        print("_", end="")
    else:
        print(letter, end="")
# For this part, it is ok to print each letter on it's own line.

# The output should look as follows:


# c
# o
# M
# M
# i
# t
# M
# e
# n
# t
# Change the print statements so that each letter is not printed 
# on its own line, but rather they are printed out next to each 
# other on the same line.

# Also, change the program to allow the user to specify the letter 
# (rather than always using "m"). Make sure your program matches 
# the letter in the word, regardless of whether the user entered 
# it as a capital or lowercase, and regardless of whether that letter 
# was a capital or lowercase in the original word.

# The output should look as follows:


# What is your favorite letter? T
# commiTmenT
# Change the program, so that instead of capitalizing the user's 
# favorite letter, it "hides" it, and replaces it with an underscore 
# in the display.

# The output should look as follows:


# What is your favorite letter? m
# co__it_ent
# Or another example could be:


# What is your favorite letter? t
# commi_men_
# Stretch Challenge
# For this part of the activity, recall the following from the 
# preparation material:

# Sometimes, when looping through the letters in a string, you might 
# want to know not only the letter, but also its position in the string. 
# In Python, you can do this using the enumerate command, which gives 
# you the position number and the letter at the same time, as follows:


# first_name = "Brigham"

# # Notice by using enumerate, we specify both i and letter
# for i, letter in enumerate(first_name):
#     print(f"The letter {letter} is at position {i}")
# The output of this code is:


# The letter B is at position 0
# The letter r is at position 1
# The letter i is at position 2
# The letter g is at position 3
# The letter h is at position 4
# The letter a is at position 5
# The letter m is at position 6
# Using this syntax, complete the following stretch challenges:

# Start a new program that will work similar to one from the core 
# requirements, but use a different string, this time using the 
# following quote from President Nelson: "In coming days, it will 
# not be possible to survive spiritually without the guiding, directing, 
# comforting, and constant influence of the Holy Ghost."
nelson_quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
# Then, instead of your program asking for a favorite letter, have it 
# ask for a number n. Make the program capitalize every n-th letter 
# in the string.
play = "yes"
while play[0] == "y":
    input_number = int(input("\nWhat is your favorite number? "))
# The output should look as follows:
    for i, letter in enumerate(nelson_quote):
        if i % input_number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")

    play = input("\nWould you like to enter another number? ").lower()

print("\nGoodbye\n")
#     Please enter a number: 3
#     In ComIng daYs, it wiLl Not be poSsiBle to suRviVe SpiRitUalLy 
# WitHouT tHe GuiDinG, DirEctIng, cOmfOrtIng, aNd ConStaNt InfLueNce 
# of thE hOly ghOst.
# Add an additional feature to your program so that the user can enter another 
# number and see it's result. To do this, you should ask the user if they would 
# like to enter another number, and continue looping as long as they type yes.

# The output should look as follows:


# Please enter a number: 3
# In ComIng daYs, it wiLl Not be poSsiBle to suRviVe SpiRitUalLy WitHouT 
# tHe GuiDinG, DirEctIng, cOmfOrtIng, aNd ConStaNt InfLueNce of thE hOly ghOst.
# Would you like to enter another number? yes
# Please enter a number: 4
# In cOminG daYs, It wIll Not Be pOssiBle To sUrviVe sPiriTualLy wIthoUt 
# tHe gUidiNg, DireCtinG, cOmfoRtinG, aNd cOnstAnt InflUencE of the holY ghOst.
# Would you like to enter another number? yes
# Please enter a number: 5
# In coMing Days, it wIll nOt be possIble To suRvive spirItualLy wiThout 
# the GuidiNg, dIrectIng, ComfoRting, and consTant InfluEnce Of thE holY ghoSt.
# Would you like to enter another number? yes
# Please enter a number: 10
# In coming Days, it wIll not be possible To survive spiritualLy without 
# the guidiNg, directIng, comfoRting, and constant Influence Of the holY ghost.
# Would you like to enter another number? no
# Goodbye