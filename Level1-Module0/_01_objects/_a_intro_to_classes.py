"""
Below is a demo of how to create and use a class in Python
Follow the instructions in the __main__ block below
For a complete reference:
https://docs.python.org/3/tutorial/classes.html
"""

import random


# This is a function. It can be used within the file and does not need
# an object of 'Duck' to be called
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


class Animal:
    pass


# Classes can inherit other classes by putting the super class inside
# parenthesis after the class name, Duck(SuperClass)
class Duck(Animal):
    # Static variables go here. They can be used using the class name,
    # Duck.num_ducks_created
    num_ducks_created = 0

    # This is a constructor! It's called when an object of this class
    # is created. The 'self' variable is always the first input parameter
    # and is used to create instance variables and call methods.
    def __init__(self, name):

        Duck.num_ducks_created = Duck.num_ducks_created + 1

        # Instance variables start with 'self.' and can only be created in
        # the constructor
        self.new_instance_variable = 'A new instance variable!'
        self.name = name

        # This is a local variable and can only be used in the constructor
        new_local_variable = 'A new local variable!'

        # Calling a method also begins with '.self'
        self.initialize()

    # This is a method!
    def initialize(self):
        # The instance variable can be used throughout the class
        print(self.name + ' the Duck was created!')


if __name__ == '__main__':
    # 1. Create an object of the Duck class
    # kenny = Duck('Kenny')

    # 2. Add 2 more input variables into the Duck constructor

    # 3. Create 2 instance variables in the Duck class

    # 4. Create 2 more methods in the Duck class,
    #    for example quack or waddle

    # 5. Create 2 more Ducks with different names and call the methods
    #    created in the previous step

    if Duck.num_ducks_created < 3:
        print('There are only ' + str(Duck.num_ducks_created) + ' Ducks.')
        print('Create more Ducks!!!')
