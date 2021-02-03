"""
Below is a demo of how to use different list methods in Python
For a complete reference:
https://docs.python.org/3/tutorial/introduction.html#lists
https://docs.python.org/3/tutorial/datastructures.html
"""
import random


if __name__ == '__main__':

    # Creating an empty list
    my_list = list()

    # Initializing a list with different objects
    my_list = [0.5, 1, 2, 3, 'welcome', 'to', 'python']

    # Initializing a list with a sequence of 50 numbers from 0 - 49
    sequential_nums_list = [num for num in range(50)]

    # Initializing a list with 50 random numbers from 0 to 100
    rand_num_list = [random.randint(0, 100) for i in range(50)]

    # Printing a list
    print(my_list)
    print(sequential_nums_list)
    print(rand_num_list)

    # Getting an element from a list
    print('element 0 from my_list: ' + str(my_list[0]))

    # Getting the size of the list
    list_len = len(my_list)
    print('size of my_list: ' + str(list_len))

    # Iterating through each element in a list
    for element in my_list:
        print(str(element))

    # Iterating through a list with an index
    for i, element in enumerate(my_list):
        print(str(i) + '. ' + str(element))

    # Alternate method to iterate through a list with an index
    for i in range(len(my_list)):
        print(str(i) + '. ' + str(my_list[i]) + ' (alternate)')

    # Removing an element from a list by index (removes last element)
    del my_list[len(my_list) - 1]

    # Removing an element from a list by value
    my_list.remove(0.5)

    print(my_list)

    # Inserting an element into an index
    my_list.insert(0, True)

    # Adding an element to the end of a list
    my_list.append('append')

    print(my_list)
