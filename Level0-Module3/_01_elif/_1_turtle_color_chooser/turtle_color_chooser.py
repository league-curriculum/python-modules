import random
import turtle
from tkinter import simpledialog

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    #      2) Make the turtle draw a shape (this will take more than one line of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for more colors & drawing them

    my_turtle = turtle.Turtle()
    my_turtle.speed(100)

    my_turtle.pensize(10)

    for i in range(5):
        color = simpledialog.askstring(title="Question", prompt="What color would you like to draw with?")

        if color == "red":
            my_turtle.pencolor("red")
        elif color == "blue":
            my_turtle.pencolor("blue")
        elif color == "yellow":
            my_turtle.pencolor("yellow")
        else:
            my_turtle.pencolor(getRandomColor())

        for i in range(3):
            my_turtle.forward(100)
            my_turtle.right(120)




    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
