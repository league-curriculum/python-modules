import tkinter as tk


# This is the setup function that will be called when the program starts
# This function will create the window and canvas and initialize the variables
# Do Not Change Anything in this function
def setup():
    window = tk.Tk()
    window.title("Ellipse Traveler")

    canvas = tk.Canvas(window, width=800, height=200, bg="white")
    canvas.pack()

    # Initialize variables
    x = [50]  # Store x in a list to pass by reference

    # Bind mouse press event to move the ellipse
    canvas.bind("<ButtonPress-1>", lambda event: on_mouse_press(event, canvas, x))

    # Draw the ellipse
    draw(canvas, x)

    window.mainloop()


# TODO 1. Create a function called draw that takes a canvas and x as parameters

# TODO 2. This function will be called by the system to draw the ellipse every 50 milliseconds so the ellipse will need to be cleared before drawing the next one. Use canvas.delete("all") to clear the canvas

# TODO 3. The function should draw an ellipse using canvas.create_oval
# Use canvas.create_oval to draw the ellipse
# The create_oval method is used to draw an oval shaped figure on the canvas. It takes five arguments: the x and y coordinates of the top left corner and the x and y coordinates of the bottom right corner of the bounding rectangle for the oval, and the fill color of the oval.  Example: canvas.create_oval(10, 10, 50, 50, fill="blue")
# In this case x is stored in a list which we will learn about later.  Use x[0] for the x coordinate of the top left corner of the ellipse and 75 for the y coordinate of the top left corner of the ellipse.  The bottom right corner of the ellipse should be x[0] + 50 and 125.  The ellipse should be filled with a color of your choice


# TODO 4. Insert this function call on the last line of the draw function:
# canvas.after(50, draw, canvas, x)


def draw(canvas, x):  # ;

    canvas.delete("all")  # ;
    canvas.create_oval(x[0], 75, x[0] + 50, 125, fill="blue")  # ;

    # Update loop
    canvas.after(50, draw, canvas, x)  # ;


# The below function is called when the mouse is pressed
# Update x[0] to change the x coordinate
# This function is called when the mouse is pressed
# Do Not call this function directly
# It is called by the system when the mouse is pressed
# Do Not Change Anything in this function
def on_mouse_press(event, canvas, x):
    x[0] += 10  # Update x[0] to change the x coordinate


# Call the setup function to start the program
setup()  # ;
