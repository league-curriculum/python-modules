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

    # Make a constructor and call the parent constructor using super().__init__()
    def __init__(self):
        super().__init__()

        # Use a tk.StringVar() variable if you want to update text on a label
        self.label_text = tk.StringVar()
        self.label_text.set("Welcome!!!")

        # Add a text label. Notice 'textvariable=' is used, not 'text=' because
        # we want to update the text on the label
        label = tk.Label(self, textvariable=self.label_text, bg='yellow', fg='blue', font=('arial', 32, 'bold'), relief='solid')

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
        self.text_field = tk.Entry(self)
        self.text_field.place(relx=0.2, rely=0.8, relwidth=0.5, height=18)

    def on_button_press(self):
        text_in_text_field = self.text_field.get()

        # Update the text in the label
        self.label_text.set(text_in_text_field)


if __name__ == '__main__':
    # Create a new object of the class
    app = MyFirstPythonApp()
    app.title('My First Python App')

    # Sets the size of the app window
    app.geometry('500x500')

    # --------------------------- Assignment --------------------------------
    # 1. Test out this app by putting text in the text field and pressing the
    # button. Does the text on the top label change?
    #
    # 2. Add another label, button, and text field in the MyFirstPythonApp
    # class. Feel free to rearrange the components in the app.

    app.mainloop()
