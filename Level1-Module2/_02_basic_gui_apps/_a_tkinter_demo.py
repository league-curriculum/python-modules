"""
Demonstration of how to make an app using Tkinter
"""
import tkinter as tk
from PIL import Image, ImageTk

# The tkinter package (“Tk interface”) is the standard Python interface to
# create GUI (Graphical User Interface) apps. The example below creates
# a window with text and an image. No work needs to be done in this file,
# but use this as a reference for future projects. For a list of all the
# things that can be added to the tkinter window, see the link below:
# https://www.tcl.tk/man/tcl8.6/TkCmd/contents.htm

def create_image(filename, width, height):
    image_obj = None

    try:
        image = Image.open(filename)
        image = image.resize((width, height), Image.ANTIALIAS)
        image_obj = ImageTk.PhotoImage(image=image)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj


# Make a new class that inherits tk.Tk
class GuiAppDemo(tk.Tk):

    # Make a constructor
    def __init__(self):

        # Call Tk class's constructor
        super().__init__()

        # Add a text label
        self.label = tk.Label(self, text="Welcome!!!", bg='yellow',
                              fg='blue', font=('arial', 32, 'bold'), relief='solid')

        # You can set the location of the label relative to the size of the window
        # The scaling will be maintained if the the app window is resized
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

        # Add an image to another label
        # *NOTE* you must save the image into a member variable and not a
        # local variable. The local variable gets garbage collected and will
        # not appear on the app:
        #   DO NOT create a local variable:: img = create_image('python.png', 200, 200)
        self.img = create_image('python.png', 200, 200)
        self.label_image = tk.Label(self, image=self.img)

        # You can set the absolute pixel location using x and y
        # The label will stay in the exact same position if the app window
        # is resized
        self.label_image.place(x=125, y=200)


if __name__ == '__main__':
    # Create the app window
    app = GuiAppDemo()

    app.title('My First Python App')

    # Sets the width x height of the app window
    app.geometry('500x500')

    # Keeps the app window open after the last instruction is executed
    app.mainloop()
