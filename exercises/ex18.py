# Exercise 18 - Names, Variables, Code, Functions
# DEFINE aka def the function
# Taking unlimited args
def print_two(*args):
# Set arg1 and arg2 to the args array
    arg1, arg2 = args
    # Print string using the two args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

def print_one(arg1):
    print("arg1: %r" % arg1)

def print_none():
    print("I got nothin'")

# Print with preset parameters
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
