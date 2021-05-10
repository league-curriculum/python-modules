"""
Creating Objects Demonstration
"""


# A variable can store more than a single item or list of items. A variable
# can store a grouping of items and functions. This kind of variable is called
# an Object. An example of an object is my_turtle below:
#   my_turtle = turtle.Turtle()
#
# The my_turtle object can access other variables, list, and functions (called
# methods) that are called using . after the object's name.
# For example:
#   my_turtle.forward(100)  # calling the forward method
#   my_turtle.left(90)      # calling the left method
#   my_turtle.forward(50)
#
# forward() and left() are both methods which are accessible to the turtle
# object. They can't be called without a turtle object like a function:
#   forward(100)    # ERROR!
#   left(90)        # ERROR!
#
# Objects are created from classes. The code inside the class determines what
# variables can be used or what methods can be called when an Object is made.
# For example:

class Dog:
    def __init__(self, name):
        self.name = name

    # Method definition within the Dog class
    def bark(self):
        print(self.name + ' barks!')


# my_dog Object named fido
my_dog = Dog('fido')
my_dog.bark()

# your_dog Object named Archimedes
your_dog = Dog('Archimedes')
your_dog.bark()
