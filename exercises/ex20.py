# Exercise #20 - Functions and Files

from sys import argv

script, input_file = argv
# Define the print_all functino with an abstract parameter `f`
def print_all(f):
    print(f.read())
# Define rewind function with `f` parameter and seek to 0
def rewind(f):
    f.seek(0)
# Define a similar function but with an additional line_count parameter
def print_a_line(line_count, f):
    # Print the number of the line and then read the line. (Creates an ordered list)
    print(line_count, f.readline())
# Set variable current_file to open the input file
current_file = open(input_file)

print("First let's print the whole file:\n")
# Print the entire current file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# Call rewind function
rewind(current_file)

print("Let's print three lines")
# Set current line value to 1 so we can add +=1 in increments 
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
