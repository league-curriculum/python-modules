"""
Use a Random object to generate random integers so your code can roll different
numbers on a dice.
"""
import tkinter as tk
from PIL import Image, ImageTk
import random


def get_random_dice_image():
    random_image = None

    # TODO Run the code and click the button. Notice that only 1 side of
    #  the die is shown.

    # TODO Change the line of code below to a random number from 1 to 6
    #  (1 and 6 included) so all 6 sides of the die are randomly shown.
    rand_num = 1

    if rand_num == 1:
        random_image = create_image('dice 1.png', 400, 400)
    elif rand_num == 2:
        random_image = create_image('dice 2.png', 400, 400)
    elif rand_num == 3:
        random_image = create_image('dice 3.png', 400, 400)
    elif rand_num == 4:
        random_image = create_image('dice 4.png', 400, 400)
    elif rand_num == 5:
        random_image = create_image('dice 5.png', 400, 400)
    elif rand_num == 6:
        random_image = create_image('dice 6.png', 400, 400)
    else:
        print("ERROR: Invalid random number!")

    return random_image

# ======================= DO NOT EDIT THE CODE BELOW =========================


def create_image(filename, width, height):
    image_obj = None

    try:
        image = Image.open(filename)
        image = image.resize((width, height), Image.ANTIALIAS)
        image_obj = ImageTk.PhotoImage(image=image)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj


class DiceRoll(tk.Tk):

    def __init__(self):
        super().__init__()

        random_image = get_random_dice_image()
        self.label_image = tk.Label(self, image=random_image)
        self.label_image.image = random_image   # To prevent garbage collection of image
        self.label_image.pack()

        self.button = tk.Button(self, text='Roll!', command=self.on_button_press)
        self.button.pack()

    def on_button_press(self):
        random_image = get_random_dice_image()
        self.label_image.config(image=random_image)
        self.label_image.image = random_image   # To prevent garbage collection of image


if __name__ == '__main__':
    # Create a new object of the class
    app = DiceRoll()
    app.title('Dice Roll')

    # Sets the size of the app window
    app.geometry('500x450')

    app.mainloop()

