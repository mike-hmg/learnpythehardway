# Exercise 19 - Functions and Variables
# defining the function `cheese_and_crackers`
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Various printing
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party")
    print("Get a blanket.\n")

print("We can just give the function numbers directly")
# Calling the function and inputting direct numbers as parameters
cheese_and_crackers(20,30)

print("OR, we can use variables from our script")
# Set variables to numbers
amount_of_cheese = 10
amount_of_crackers = 50
# Use variables instead of directly inputting numbers as parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# Add a little math in there
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables, and math:")
# Combining the above in more complex format
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
