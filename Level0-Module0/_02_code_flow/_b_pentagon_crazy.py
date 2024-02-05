import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


def getNextColor(i):
    return colors[i % len(colors)]


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=0.75, height=0.9, startx=0, starty=0)

colors = ("red", "blue", "green", "yellow", "orange")

# Make a new turtle
myTurtle = turtle.Turtle()  # ;

# Make the turtle shape 'turtle', .shape('turtle')
myTurtle.shape("turtle")  # ;

# Set the turtle speed to max (0)
myTurtle.speed(0)  # ;

# Set the turtle width to 1
myTurtle.width(1)  # ;

# Create a variable to hold the number of sides in a pentagon
sides = 5  # ;

# Create a variable to be the angle of 360 divided by the sides variable
angle = 360 / sides  # ;

# Use a for loop to repeat ALL the following lines of code 360 times.
for i in range(360):  # ;

    # If the loop variable (i) is equal to 100, set the turtle width to 2
    if i == 100:  # ;
        myTurtle.width(2)  # ;

    # If the loop variable (i) is equal to 200, set the turtle width to 3
    if i == 200:  # ;
        myTurtle.width(3)  # ;

    # Use the getNextColor function to set the turtle pencolor,
    # *hint .pencolor(getNextColor(i))
    myTurtle.pencolor(getNextColor(i))  # ;

    # Move the turtle forward by the loop variable, *hint .forward(i)
    myTurtle.forward(i)  # ;

    # Turn the turtle to the right by the angle variable + 1
    myTurtle.right(angle + 1)  # ;

# Hide your turtle so you can see the pattern.
myTurtle.hideturtle()  # ;

# Check the pattern against the picture in the recipe. If it matches, you are done!

# Variations:
# *Make the pattern really huge
# *Change the colors
# *Experiment with different shapes

# call the turtle .done() method
turtle.done()  # ;
