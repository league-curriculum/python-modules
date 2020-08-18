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


# Make a new class called MyFirstPythonApp that inherits tk.Tk, example:
class MyFirstPythonApp(tk.Tk):

    # Make a constructor
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)

        # Add a text label
        label = tk.Label(self, text='Welcome!!', bg='yellow', fg='blue', font=('arial', 32, 'bold'), relief='solid')

        # You can set the location
        # label.place(x=25, y=25)
        label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

        # Add an image
        img = create_image('python.png', 200, 200)
        label_image = tk.Label(self, image=img)
        label_image.image = img
        label_image.place(x=125, y=200)

        # Add a button
        button = tk.Button(self, text='Press Me!', bg='green', fg='black', command=lambda: self.on_button_press())
        button.place(x=200, y=450)

        # Add a text field
        self.text_field = tk.Entry(self, text="<Enter some text here>")
        self.text_field.place(relx=0.2, rely=0.8, relwidth=0.5, height=18)

    def on_button_press(self):
        print(self.text_field.get())


if __name__ == '__main__':
    app = MyFirstPythonApp(None)
    app.title('My First Python App')
    app.geometry('500x500')
    app.mainloop()
