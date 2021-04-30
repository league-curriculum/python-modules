"""
Demonstration of lists
"""
import random

# lists are like variables except instead of containing a single item they
# can contain a varying number of items. For example, we can create a variable
# that contains a string for a name:
#   name = "Michelle"
#
# A list can hold multiple names using the square brackets ([, ]) like so:
#   names = ["Michelle", "Demir", "Khang"]
#
# In this case, names contains 3 names, "Michelle", "Demir", and "Khang".
# To get a single name from the names list use the list name, the
# square brackets, and the index, which is a number starting at 0:
#   print(names[0])   # prints Michelle
#   print(names[1])   # prints Demir
#   print(names[2])   # prints Khang
#
# The first item added (starting from the left) is index 0, the next is
# index 1, then index 2, and so on...
#   names = ["Michelle", "Demir", "Khang"]
#   # index      0          1        2
#
# lists do not always have to contain the same kind of item. For example:
#   my_turtle = turtle.Turtle()
#   stuff = [1, "books", 3.14, my_turtle]

# If it can be put into a variable, it can be put into a list.
#

if __name__ == '__main__':

    # Creating an empty list (no items). Use if you don't immediately know
    # what to put in your list
    my_empty_list = list()

    # Initializing a list with different objects
    my_list = [0.5, 1, 2, 3, 'welcome', 'to', 'python']

    # Getting an item from a list
    my_item = my_list[4]
    print('The item at index 4 is: ' + str(my_item))

    # Changing an item in a list
    my_list[4] = 'CHANGED!'
    my_item = my_list[4]
    print('The item at index 4 is now: ' + str(my_item))

    # Getting the current number of items in the list
    num_items = len(my_list)
    print('There are ' + str(num_items) + ' items in     ' + repr(my_list))

    # Adding an item to the end of a list
    my_list.append('NEW ITEM')
    num_items = len(my_list)
    print('There are now ' + str(num_items) + ' items in ' + repr(my_list))

    # Removing the first matching item from a list
    # *Note* If there are the one with the lowest index is removed
    my_list.remove('NEW ITEM')
    num_items = len(my_list)
    print('There are now ' + str(num_items) + ' items in ' + repr(my_list))

    # Iterating (looping) through all the items in the list
    for item in my_list:
        print(item, end=' ')

    print()

    # Method #1: Iterating (looping) through all items in list with an index
    num_items = len(my_list)
    for index in range(num_items):
        print(index, my_list[index], end='; ')

    print()

    # Method #2: Iterating (looping) through all items in list with an index
    for index, item in enumerate(my_list):
        print(index, item, end='; ')
