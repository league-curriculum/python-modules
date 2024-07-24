"""
 Create an app that tells a joke, then a punchline
"""
import tkinter as tk
import random
from tkinter import messagebox


# Use this function to return a random character
def generate_random_letter():
    return chr(random.randint(0, 25) + ord('a'))


class ChuckleClicker(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize 2 buttons (tk.Button)
        #  one button for the joke and another for the punchline
        self.joke = tk.Button(self, text='joke', fg='black',
                              font=('arial', 32, 'bold'), relief='solid')

        self.punchline = tk.Button(self, text='punchline', fg='black',
                                   font=('arial', 32, 'bold'), relief='solid')

        # TODO: Place the 2 buttons next to each other (see example image)
        self.joke.place(relx=0, rely=0, relwidth=0.5, relheight=1.0)
        self.punchline.place(relx=0.5, rely=0, relwidth=0.5, relheight=1.0)

        # TODO: Call the joke button's bind() method to call the on_joke()
        #  method when a mouse button is pressed
        #  example: self.joke_button.bind('<ButtonPress>', self.on_joke)
        self.joke.bind('<ButtonPress>', self.on_joke)

        # TODO: Call the joke button's bind() method to call the on_punchline()
        #  method when a mouse button is pressed
        self.punchline.bind('<ButtonPress>', self.on_punchline)

    def on_joke(self, event):
        print('Joke button pressed')

        # TODO: Write your joke below!
        messagebox.showinfo(None, "So a man walks into a bar...")

    def on_punchline(self, event):
        print('Punchline button pressed')

        # TODO: Write a punchline to your joke!
        messagebox.showinfo(None, "Ouch!")



# TODO: Create a new ChuckleClicker object and set the title and geometry.
#  Remember to call mainloop() at the end
game = ChuckleClicker()
game.title('Chuckle Clicker')
game.geometry('600x400')
game.mainloop()
