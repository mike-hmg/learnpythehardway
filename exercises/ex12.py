# Exercise #12 - Adding some more functionality
## See Exercise 11 for comparison on this.
## Setting a placeholder text. This is a much cleaner approach to capturing user input
age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weight?")

print("So, you are %r old, %r tall and %r heavy." % (age, height, weight))
