"""
In this lesson we will learn about classes and the 'self' parameter.  Classes are a way to group functions and variables together.  The 'self' parameter is used to access the variables and functions within the class.  The 'self' parameter connects the functions and variables to the class.  With 'self' we can make an instance of the class and with that instance we can access the functions and variables within the class.  When we use functions in a class we call them methods.  All the references to functions below will be called methods.
"""

import tkinter as tk
from random import randint


# TODO 1. Read the comments carefully and complete the code below
class IceCreamShop:
    """
    Notice that the __init__ method has a parameter called 'window', not all __init__ methods have a window parameter, in this case it is needed to reference the tkinter window.  window is the window that the class will be displayed in.  The __init__ method is a special method that is called when an instance of the class is created.  The __init__ method is used to initialize the variables and functions within the class.  The 'self' parameter is used to access the variables and functions within the class.
    """

    def __init__(self, window):
        self.window = window
        self.canvas_width = 500
        self.canvas_height = 500
        self.coneY = 320
        self.scoops = []
        self.sprinkles = []

        self.canvas = tk.Canvas(
            window, width=self.canvas_width, height=self.canvas_height
        )
        self.canvas.pack()

        # TODO 2. call the make_ice_cream_cone method.  Remember to use the 'self' parameter
        self.make_ice_cream_cone()  # ;

        self.window.after(50, self.sprinkle_fall)

    # This method is used to add a scoop of ice cream to the cone.  Do not change this method
    def add_scoop(self, flavor):
        if flavor.lower() == "chocolate":
            color = "#744710"
        elif flavor.lower() == "strawberry":
            color = "#E88E81"
        elif flavor.lower() == "vanilla":
            color = "#F5F3E3"
        else:
            print(f"ERROR: We don't have the flavor {flavor}")
            return

        self.scoops.append(
            (
                self.canvas.create_oval(
                    self.canvas_width / 2 - 75,
                    self.coneY - 150,
                    self.canvas_width / 2 + 75,
                    self.coneY,
                    fill=color,
                ),
                color,
            )
        )

    # This method is used to add sprinkles to the ice cream cone.  Do not change this method
    def add_sprinkle(self, number_of_sprinkles):
        for _ in range(number_of_sprinkles):
            x_pos = randint(self.canvas_width / 2 - 75, self.canvas_width / 2 + 75)
            y_pos = randint(0, self.canvas_height / 2)
            sprinkle_color = "#{:02x}{:02x}{:02x}".format(
                randint(0, 255), randint(0, 255), randint(0, 255)
            )
            sprinkle = self.canvas.create_oval(
                x_pos, y_pos, x_pos + 5, y_pos + 5, fill=sprinkle_color
            )
            self.sprinkles.append((sprinkle, x_pos, y_pos))

    # This method is used to make the sprinkles fall.  Do not change this method
    def sprinkle_fall(self):
        for idx, (sprinkle, x_pos, y_pos) in enumerate(self.sprinkles):
            self.canvas.move(sprinkle, 0, 5)
            y_pos += 5
            self.sprinkles[idx] = (sprinkle, x_pos, y_pos + 15)
        if any(y_pos < self.coneY for _, _, y_pos in self.sprinkles):
            self.window.after(50, self.sprinkle_fall)

    def add_cherry(self):  # ;
        self.canvas.create_oval(240, 150, 260, 170, fill="red")  # ;

    def make_ice_cream_cone(self):
        self.canvas.create_polygon(190, self.coneY, 310, 300, 255, 500, fill="#BC7E31")

        # TODO 3. Call the add_scoop method with your choice of chocolate, vanilla or strawberry.  Remember to use the 'self' parameter
        self.add_scoop("chocolate")  # ;

        # TODO 4. Call the add_sprinkle method with the number of sprinkles you want.
        self.add_sprinkle(100)

        # TODO 5. Can you create a method that adds a cherry on top of the ice cream cone and add a call to it here?
        self.add_cherry()  # ;


root = tk.Tk()
ice_cream_shop = IceCreamShop(root)
root.mainloop()
