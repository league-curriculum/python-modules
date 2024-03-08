"""
When This program is completed there will be moles drawn in each hole.  The moles will be drawn using the create_oval method of the canvas object.
"""

# TODO 1. Import the tkinter library as tk
import tkinter as tk  # ;


# This is the setup function that will be called when the program starts
def setup():
    # TODO 2. Create a window object and set the title to "Moles in Holes". You can reference previous recipes for help
    window = tk.Tk()  # ;
    window.title("Moles in Holes")  # ;
    # TODO 3. Create a canvas object and set the width to 400 and the height to 400. You can reference previous recipes for help
    canvas = tk.Canvas(window, width=400, height=400)  # ;
    canvas.pack()  # ;

    # This is the code that will draw the holes
    canvas.create_oval(150, 170, 250, 200, fill="black")
    canvas.create_oval(20, 89, 120, 119, fill="black")
    canvas.create_oval(150, 30, 250, 60, fill="black")
    canvas.create_oval(147, 320, 247, 350, fill="black")
    # Go to TODO 4 before you complete these steps
    # TODO 6. Call the draw_mole function four times to draw a mole in each hole.  The first mole should be drawn at coordinats: 250, 50. You will need to figure out the coordinates for the other moles
    draw_mole(canvas, 250, 50)  # ;
    draw_mole(canvas, 20, 100)  # ;
    draw_mole(canvas, 150, 175)  # ;
    draw_mole(canvas, 250, 325)  # ;

    # TODO 7. Call the mainloop method of the window object.  You can reference previous recipes for help
    window.mainloop()


# TODO 4. Create a function called draw_mole that takes a canvas, mole_x, and mole_y as parameters
# TODO 5. In the draw_mole function, use the create_oval method to draw the mole.  The create_oval method is used to draw an oval shaped figure on the canvas. It takes five arguments: the x and y coordinates of the top left corner and the x and y coordinates of the bottom right corner of the bounding rectangle for the oval, and the fill color of the oval.  Example: canvas.create_oval(10, 10, 50, 50, fill="blue").  Create Ovals for the mole's face, nose, eyes, and mouth.  The mole's face should be centered at mole_x, mole_y and have a radius of 30.
# Hint:  Use the draw_mole arguments to calculate the coordinates for the ovals
def draw_mole(canvas, mole_x, mole_y):  # ;

    mole_face = canvas.create_oval(
        mole_x - 30, mole_y - 30, mole_x + 30, mole_y + 30, fill="#7D5D2B"  # ;
    )
    mole_nose = canvas.create_oval(
        mole_x - 5, mole_y - 10, mole_x + 5, mole_y, fill="black"  # ;
    )
    mole_eyes = canvas.create_oval(
        mole_x - 20, mole_y - 25, mole_x - 10, mole_y - 15, fill="black"  # ;
    )
    mole_eyes = canvas.create_oval(
        mole_x + 10, mole_y - 25, mole_x + 20, mole_y - 15, fill="black"  # ;
    )
    mole_mouth = canvas.create_oval(
        mole_x - 10, mole_y, mole_x + 10, mole_y + 5, fill="black"  # ;
    )


# TODO 8. Call the setup function to start the program
setup()
