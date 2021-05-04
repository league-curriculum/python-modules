"""
My first Python app using Tkinter
"""
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


# TODO 1) Make a new class and put tk.Tk in the parenthesis, for example:
class MyFirstApp(tk.Tk):

    # TODO 2) Make a constructor
    def __init__(self):
        # TODO 3) Call the Tk class's constructor
        super().__init__()

        # TODO 4) Add a text label and pick a text message to display
        self.label = tk.Label(self, text='Text!', bg='yellow', fg='blue',
                              font=('arial', 32, 'bold'), relief='solid')

        # TODO 5) Place the label somewhere on your app. You can use either
        #  x and y or relx and rely
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

        # TODO 6) Create an image variable using the create_image function
        #  you can use the image provided in the folder or another image
        #  from the internet
        self.img = create_image('python.png', 200, 200)

        # TODO 7) Create another label and attach to it the image object
        #  from the previous step
        self.label_image = tk.Label(self, image=self.img)

        # TODO 8) Place the label somewhere on your app
        self.label_image.place(x=125, y=200)


# TODO 9) Create an if __name__ == '__main__': block
if __name__ == '__main__':
    # TODO 10) Create an object of your app class
    app = MyFirstApp()

    # TODO 11) Use the app object to set a title
    app.title('My First Python App')

    # TODO 12) Use the app object to set the window dimensions (width x height)
    app.geometry('500x500')

    # TODO 13) Run the app object's mainloop() method
    app.mainloop()
