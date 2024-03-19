import tkinter as tk
from PIL import Image, ImageTk
import os

"""
In this lesson we will build a game called "Pin the Tail on the Donkey". A lot of the code is already written for you. Read the TODOs and complete the code as instructed.
"""


class PinTheTailOnTheDonkey:
    """
    A class representing a game called "Pin the Tail on the Donkey".

    Attributes:
        window: The main window of the game.
        donkey_img_path: The file path of the donkey image.
        tail_img_path: The file path of the tail image.
        canvas: The canvas where the game is displayed.
        tail_id: The ID of the tail image on the canvas.
        donkey_id: The ID of the donkey image on the canvas.
    """

    def __init__(self, window):
        """
        Initializes a new instance of the PinTheTailOnTheDonkey class.

        Args:
            window: The main window of the game.
        """
        self.window = window
        self.window.geometry("800x600")
        self.window.title("Pin the Tail on the Donkey")

        self.donkey_img_path = os.path.join(os.path.dirname(__file__), "donkey.jpg")
        self.tail_img_path = os.path.join(os.path.dirname(__file__), "tail.png")
        # TODO 1) call the setup_canvas method here, use the self keyword to call the method.
        self.setup_canvas()  # ;
        self.tail_id = None
        self.donkey_id = None

    def setup_canvas(self):
        """
        Sets up the canvas for the game.
        """
        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack()

        donkey_img = Image.open(self.donkey_img_path).resize((800, 600))
        self.donkey = ImageTk.PhotoImage(donkey_img)

        tail_img = Image.open(self.tail_img_path)
        self.tail = ImageTk.PhotoImage(tail_img)

        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release)

    def mouse_click(self, event):
        """
        Handles the mouse click event on the canvas.

        Args:
            event: The mouse click event.
        """
        # TODO 2) check if the tail_id attribute is not None, if it is not None, delete the tail image from the canvas. Use the self keyword to access the tail_id attribute. Use the canvas.delete method to delete the tail image from the canvas and remember the self keyword.
        if self.tail_id:
            self.canvas.delete(self.tail_id)

        self.tail_id = self.canvas.create_image(
            event.x, event.y, anchor="center", image=self.tail
        )

    def mouse_release(self, event):
        """
        Handles the mouse release event on the canvas.

        Args:
            event: The mouse release event.
        With the event we can access the x and y coordinates of the mouse click.  We can use these coordinates to determine if the tail is placed on the back of the donkey or not. If the tail is placed on the back of the donkey, we will display the donkey image. If the tail is not placed on the back of the donkey, we will delete the tail image from the canvas.
        """
        # TODO 3) Check if self.tail_id is not None.  
        if self.tail_id:
            # HINT for the following: There will be nested if statements.
            # TODO 4) Check if the x and y coordinates of the mouse click are within the range of the donkey's back. The x coordinates should be between 680 and 730 and the y coordinates should be between 250 and 350.
            # TODO 5) If the tail is placed on the back of the donkey, display the donkey image on the canvas. Use the self keyword to access the donkey_id attribute and the canvas.create_image method to display the donkey image on the canvas. Remember to use the self keyword.  Else, delete the tail image from the canvas. Use the canvas.delete method to delete the tail image from the canvas and remember the self keyword.
        if self.tail_id:
            if 680 <= event.x < 730 and 250 <= event.y < 350:
                if self.donkey_id:
                    self.canvas.delete(self.donkey_id)
                self.donkey_id = self.canvas.create_image(
                    400, 300, anchor="center", image=self.donkey
                )
            else:
                self.canvas.delete(self.tail_id)


# DO NOT CHANGE THE CODE BELOW
root = tk.Tk()
PinTheTailOnTheDonkey(root)
root.mainloop()
