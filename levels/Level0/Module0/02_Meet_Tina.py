# Here is a simple Turtle program that draws a square and writes a message.
# The lines that start with a # are comments. They are not executed by Python.
# Comments are used to explain what the code does.
# Read the program and try to understand what each line does.

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle

forward = 150                           # Set the forward distance to 150
left = 90                               # Set the left turn to 90 degrees

tina.forward(forward)                   # Move tina forward by the forward distance
tina.left(left)                         # Turn tina left by the left turn

tina.forward(forward)                   # Continuie the last two steps three more times
tina.left(left)                         # to draw a square

tina.forward(forward)
tina.left(left)

tina.forward(forward)
tina.left(left)

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.forward(20)                        # Move tina forward by 20
tina.left(left)                         # Turn tina left by 90 degrees
tina.forward(20)                        # Move tina forward by 20
tina.write("Why, hello there!")         # Write the message "Why, hello there!"
tina.backward(20)                       # Move tina backward by 20

turtle.exitonclick()                    # Close the window when we click on it