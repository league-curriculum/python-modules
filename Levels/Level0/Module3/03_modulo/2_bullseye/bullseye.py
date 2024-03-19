# TODO 1) Import the tkinter module as tk
import tkinter as tk

# TODO 2) Create a function called draw_bullseye that takes a canvas as a parameter
# TODO 3) Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses.  Use canvas.create oval to draw the ellipses.  The ellipses should be centered at (250, 250) and the width and height should be the same.  The width and height should start at 200 and decrease by 25 each time through the loop.
# TODO 4) Use the modulo operator to change the color of the ellipses.  If the index of the for loop is even, use the color "red", otherwise use the color "black".


def draw_bullseye(canvas):
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    for i in range(200, 10, -25):
        if i % 2 == 0:
            color = "red"
        else:
            color = "black"
        canvas.create_oval(
            250 - i / 2, 250 - i / 2, 250 + i / 2, 250 + i / 2, fill=color
        )


# DO NOT EDIT THE CODE BELOW
def setup():
    # Set up the tkinter window
    window = tk.Tk()
    window.title("Bullseye")
    canvas = tk.Canvas(window, width=500, height=500)
    canvas.pack()
    draw_bullseye(canvas)
    window.mainloop()


setup()
