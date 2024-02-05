"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle


def square(my_turtle, x, y, length):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(90)


def triangle(my_turtle, x, y, length):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    for i in range(3):
        my_turtle.forward(length)
        my_turtle.right(180 - 60)


def circle(my_turtle, x, y, radius):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.circle(radius, 360, 20)



# TODO) This recipe practices writing and calling functions.
#  1. Create a turtle.
#  2. Write 3 method definitions for drawing a square, triangle, and
#     circle.
#  3. Ask the user for the for a shape to draw.
#  4. Draw the appropriate shape depending on their answer (call the right
#     function)
t = turtle.Turtle()
t.shape('turtle')

window = Tk()
window.withdraw()

while True:
    shape = simpledialog.askstring(None, 'What shape do you want to draw?')

    if shape.lower() == 'circle':
        circle(t, -100, 100, 50)
    elif shape.lower() == 'triangle':
        triangle(t, 100, 100, 50)
    elif shape.lower() == 'square':
        square(t, 100, -100, 50)
    else:
        break

turtle.done()
