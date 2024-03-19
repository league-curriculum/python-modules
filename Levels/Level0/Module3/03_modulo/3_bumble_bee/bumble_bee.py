# TODO 1) Import the tkinter module as tk
import tkinter as tk  # ;


# Do not edit the code below.  You will use this function later in the assignment.
def draw_flower(canvas):
    # Define the position of the flower
    x = 50
    y = 450

    # Draw stem
    stem_x = x
    stem_y = y + 100
    canvas.create_rectangle(
        stem_x - 5, stem_y, stem_x + 5, y, fill="#228B22", outline="#228B22"
    )

    # Draw petals in a hexagon pattern
    petal_color = "#FFD700"  # Gold
    petal_size = 20
    petal_offsets = [(0, -25), (15, -10), (15, 20), (0, 35), (-15, 20), (-15, -10)]
    for offset in petal_offsets:
        petal_x, petal_y = x + offset[0], y + offset[1]
        canvas.create_oval(
            petal_x - petal_size,
            petal_y - petal_size,
            petal_x + petal_size,
            petal_y + petal_size,
            fill=petal_color,
        )

    # Draw center of flower
    canvas.create_oval(
        x - 15, y - 15, x + 15, y + 15, fill="#FF4500", outline="#FF4500"
    )


# Do not edit the code below.  You will use this function later in the assignment.
def draw_bee_face(canvas, x, y):
    # draw bee's face
    canvas.create_line(x - 10, y - 27, x - 17, y - 50, fill="black", width=5)
    canvas.create_line(x + 10, y - 27, x + 17, y - 50, fill="black", width=5)
    canvas.create_oval(x - 17 - 5, y - 50 - 5, x - 17 + 5, y - 50 + 5, fill="black")
    canvas.create_oval(x + 17 - 5, y - 50 - 5, x + 17 + 5, y - 50 + 5, fill="black")
    canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill="#FFFB1C")  # face
    canvas.create_oval(x - 20, y - 25, x - 5, y - 10, fill="black")  # eyes
    canvas.create_oval(x + 5, y - 25, x + 20, y - 10, fill="black")
    canvas.create_oval(x - 5, y, x + 5, y + 10, fill="black")  # nose
    canvas.create_oval(x - 10, y + 5, x + 10, y + 15, fill="#FFFB1C")  # mouth


# TODO 2) Create a function called draw that takes a canvas as a parameter
# TODO 3) Use a for loop to draw a grid of circles.  The circles should be centered at (i, j) where i and j are multiples of 25.  The circles should have a radius of 25.  Use the modulo operator to change the color of the circles.  If i + j is even, use the color "yellow" = "#FFFF00", otherwise use the color "black" = "#000000".
# TODO 4) Call the draw_bee_face function to draw the bee's face at (400, 400).
def draw(canvas):  # ;
    for i in range(0, 400, 25):  # ;
        if i % 2 == 0:  # ;
            color = "#FFFF00"  # ;
        else:
            color = "#000000"  # ;
        canvas.create_oval(i - 25, i - 25, i + 25, i + 25, fill=color)  # ;

    draw_bee_face(canvas, 400, 400)  # ;


def setup():
    # These lines set up the tkinter window
    window = tk.Tk()
    window.title("Bee and Flowers")
    canvas = tk.Canvas(window, width=500, height=500, bg="#A0A0A0")
    canvas.pack()
    # TODO 5) Call the draw_flower function and use the canvas as a parameter
    draw_flower(canvas)  # ;
    # TODO 6) Call the draw function and use the canvas as a parameter
    draw(canvas)  # ;
    # TODO 7) Call the window.mainloop() function
    window.mainloop()  # ;


# TODO 8) Call the setup function
setup()  # ;
