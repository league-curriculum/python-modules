import tkinter as tk
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


# Make a new class that inherits tk.Tk
class MyFirstPythonApp(tk.Tk):

    # Make a constructor and call the parent constructor using super().__init__(parent)
    def __init__(self, parent):
        super().__init__(parent)

        # Add a text label
        label = tk.Label(self, text='Welcome!!', bg='yellow', fg='blue', font=('arial', 32, 'bold'), relief='solid')

        # You can set the location of the label relative to the size of the window
        # The scaling will be maintained if the the app window is resized
        label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

        # Add an image
        img = create_image('python.png', 200, 200)
        label_image = tk.Label(self, image=img)
        label_image.image = img

        # You can set the absolute pixel location using x and y
        label_image.place(x=125, y=200)

        # Add a button.
        # command=lambda: self.on_button_press() tells the program to call the
        # on_button_press() method when the button is clicked
        button = tk.Button(self, text='Press Me!', bg='green', fg='black', command=lambda: self.on_button_press())
        button.place(x=200, y=450)

        # Add a text field
        self.text_field = tk.Entry(self, text="<Enter some text here>")
        self.text_field.place(relx=0.2, rely=0.8, relwidth=0.5, height=18)

    def on_button_press(self):
        print(self.text_field.get())


if __name__ == '__main__':
    # Create a new object of the class
    app = MyFirstPythonApp(None)
    app.title('My First Python App')

    # Sets the size of the app window
    app.geometry('500x500')

    # --------------------------- Assignment --------------------------------
    # Add another label, button, and text field in the MyFirstPythonApp class

    app.mainloop()
