import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 

for i in range(4):
    tina.forward(150)                   # Move tina forward by the forward distance
    tina.left(90)                       # Turn tina left by the left turn

# Move tina away from the square
tina.penup()
tina.goto(-100, 100)
tina.pendown()

for i in range(5):
    tina.forward(60)                    # Move tina forward by the forward distance
    tina.left(360/5)                    # Turn tina left by the left turn

