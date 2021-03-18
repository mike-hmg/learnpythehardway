# Exercise 31 - Making interactive functions and if statements.

# Print the first user interactive questions to go to STDOUT

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

# Prompt user for input in the terminal
door = raw_input("Enter 1/2 > ")

# If user enters "1", give more options to select
if door == "1":
    print "Theres a giant bear her eating a cheesecake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    # Prompt user for second choice
    bear = raw_input("> ")
    # If the choose "1". Print message.
    if bear == "1":
        print "The bear eats your face off. Good job!"
    # If the choose "2". Print message.
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    # If anything else is used as the input. Repeat their selection to them with statement.
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
# If they initially went through door #2...
elif door == "2":
    print "You start into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    # Ask for second choice
    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
# Close the entire if statement
else:
    print "You stumble around and fall on a knife and die. Good job!"
