# Tina The Turtle from https://trinket.io/eric-busboom/courses/introduction-to-python-programming

# The import statement tells python that we want to use the turtle module.
# a module is a collection of code that is stored in a file.
import turtle

# The first 'turtle' is the name of the module, and the second 'Turtle'
# is another group of code cladded a 'class'. The 'Turtle' class has code
# that allows us to create a turtle
#
# The equals sign means that we are giving the turtle a name, 'tina'.
tina = turtle.Turtle()

# the '.shape' part of this line is called a method, sometimes known as a function.
# This method tells the turtle what shape to have. The 'tina.shape' part
# means that we want to change the shape of tina.
tina.shape('turtle')

# Read the following lines and see if you can figure out what they do.
tina.penup()
tina.forward(20)
tina.write("Why, hello there!")
tina.backward(20)
