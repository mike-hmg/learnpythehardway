# Exercise 32 - Loops and Lists

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This loop counts for every 'number' in the array
for number in the_count:
    print "This is count %d" % number

for x in fruits:
    print "A fruit of type: %s" % x

# Here's a mixed list. Note the use of %r for raw instead of %d or %s
for i in change:
    print "I got %r" % i

# building lists with .append()
# set blank array
elements = []

# Use range fundtion to do 0 - 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function to add to the lists
    elements.append(i)

# now we can print them out
for i in elements:
    print "Element was: %d" % i
