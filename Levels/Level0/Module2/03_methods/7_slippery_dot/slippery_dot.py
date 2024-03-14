"""
In this lesson you will learn how to initialize class variables and use them in methods.  You will also learn how to create an instance of a class and call its methods.
"""

import tkinter as tk
import math
import random


class Sketch:
    # TODO 0. Create an __init__ method that takes self, and a canvas parameters
    def __init__(self, canvas):  # ;
        # TODO 1. Create a class variable called canvas and set it to the canvas parameter
        self.canvas = canvas  # ;
        # TODO 2. Create 3 more class variables called x, y, and sz and set them to 100
        self.x = 100  # ;
        self.y = 100  # ;
        self.sz = 100  # ;

    def draw(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 500, 500, fill="blue")
        # TODO 3. Create an oval at the x and y position with a size of sz, and fill it with white.  Use the create_oval method of the canvas object.
        self.canvas.create_oval(
            self.x, self.y, self.x + self.sz, self.y + self.sz, fill="white"
        )  # ;

    def mousePressed(self, event):
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 400)
        self.draw()
        # TODO 4. Create a variable called distance and set it to the result of calling the getDistanceFromMouse method with the x and y position as parameters
        distance = self.getDistanceFromMouse(self.x, self.y)  # ;
        # TODO 5. Print the distance variable to the console using the print function
        print("Distance:", distance)  # ;

    def getDistanceFromMouse(self, x, y):
        dx = self.canvas.canvasx(self.canvas.winfo_pointerx()) - x
        dy = self.canvas.canvasy(self.canvas.winfo_pointery()) - y
        return math.sqrt(dx**2 + dy**2)


window = tk.Tk()
window.title("Slippery Dot")

canvas = tk.Canvas(window, width=500, height=500, bg="blue")
canvas.pack()

# TODO 6. Create a variable called sketch and set it to an instance of the Sketch class with the canvas as a parameter
sketch = Sketch(canvas)  # ;

canvas.bind("<Button-1>", sketch.mousePressed)

# TODO 7. Call the mainloop method of the window object
window.mainloop()  # ;

# TODO 8. Run your code and move the dot around the screen.  You should see the distance printed to the console each time you click the mouse.
