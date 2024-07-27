# Here is a simple Turtle program that draws a square and writes a message.
# The lines that start with a # are comments. They are not executed by Python.
# Comments are used to explain what the code does.
# Read the program and try to understand what each line does.

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 
forward = 150                           # Set the forward distance to 150
left = 90                               # Set the left turn to 90 degrees

tina.pencolor('blue')                   # Set the pen color to blue
tina.forward(forward)                   # Move tina forward by the forward distance
tina.left(left)                         # Turn tina left by the left turn

tina.pencolor('red')                    # Set the pen color to red
tina.forward(forward)                   # Continuie the last two steps three more times
tina.left(left)                         # to draw a square

tina.pencolor('green')                  # Set the pen color to green
tina.forward(forward)
tina.left(left)

tina.pencolor('purple')                 # Set the pen color to purple
tina.forward(forward)
tina.left(left)

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.forward(20)                        # Move tina forward by 20
tina.left(left)                         # Turn tina left by 90 degrees
tina.forward(20)                        # Move tina forward by 20
tina.write("Why, hello there!")         # Write the message "Why, hello there!"
tina.backward(20)                       # Move tina backward by 20

tina.pendown()
tina.color('red')                       # Set the color of tina to red
tina.begin_fill() 
tina.circle(100, steps=50)
tina.end_fill() 

turtle.exitonclick()                    # Close the window when we click on it