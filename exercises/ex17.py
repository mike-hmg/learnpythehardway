# Exercise 17 - More Files
# import argv
from sys import argv
# import `exists` from the os.path
from os.path import exists
# Set first 3 elements in the array to script, from_file, and to_file
script, from_file, to_file = argv
# Print that we're copying file to file
print("Copying from %s to %s" % (from_file, to_file))
# Open from_file and set it to vairable in_file
in_file = open(from_file)
# Read the file and set the data to `indata`
indata = in_file.read()
# Print message that uses len to state how many bytes the file is
print("The input file is %d bytes long" % len(indata))
# Use `exists` import to see if file exists or not
print("Does the output file exist? %r" % exists(to_file))
# Message to continue or not, followed by a prompt for user
print("Ready, hit RETURN to continue, CTRL-C (^C) to abort.")
# Collect input
input()
# set new var `out_file` to an the old to_file with write permissions
out_file = open(to_file, 'w')
# write indata to out_file
out_file.write(indata)
# Confirmation message
print("Alright, all done.")
# Close files
out_file.close()
in_file.close()
