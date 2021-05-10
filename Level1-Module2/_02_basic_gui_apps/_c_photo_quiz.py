"""
Photo Quiz: Ask a question about a photo and guess the answer!
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL import Image, ImageTk

def create_image(filename, width, height):
    image_obj = None

    try:
        image = Image.open(filename)
        image = image.resize((width, height), Image.ANTIALIAS)
        image_obj = ImageTk.PhotoImage(image=image)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj

# ======================= DO NOT EDIT THE CODE ABOVE =========================

# TODO 0) Find at least 3 interesting photos (2 are provided if you want
#  to use those)

# TODO 1) Create a new tkinter class

    # TODO 2) Create a constructor

        # TODO 3) call Tk's constructor

        # TODO 4) Create a member variable for a label and place it.
        #  You do not need to add any text or images to the label.


# TODO 5) Create an if __name__ == '__main__': block

    # TODO 6) Create an object of the tkinter class

    # TODO 7) Set the app window width and height using geometry()

    # TODO 8) Declare and initialize a score variable

    # TODO 9) Create an image object variable using the create_image function
    #  above and store it in a variable

    # TODO 10) Set the image onto the class's label using the configure method,
    #  for example:
    #  app.photo_label.configure(image=image_object)

    # TODO 11) Use a pop-up (simpledialog) to ask the user a question
    #  relating to the image and tell them if they get the right answer.

    # TODO 12) If the answer is correct, increase the score by 1

    # TODO 13) Repeat the steps to show a different photo and ask a different
    #  question

    # TODO 14) Display the score to the user after asking the last question
