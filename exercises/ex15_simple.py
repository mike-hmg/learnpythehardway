# Simpler version to just prompt and print whatever file is input
from sys import argv

print("What file do you want me to read?")
filename = input("> ")
txt = open(filename)
print(txt.read())
