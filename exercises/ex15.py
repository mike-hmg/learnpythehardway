from sys import argv # Importing the "sys.argv" module

script, filename = argv
# `script` is set to 0 in the argv array and `filename` sets to 1 in the array

txt = open(filename)
# Takes file from parameter and sets to variable `txt`

print("Here's your file %r: " % filename)
# Prints out the greeting along with filename
print(txt.read())
# Takes the `txt` variable and reads the actual file
print("Type the filename again: ")
file_again = input("> ")
# Prompts user to input the filename
txt_again = open(file_again)
# Opens file and sets to the variable
print(txt_again.read())
# Read the file and print the contents
