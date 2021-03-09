"""
Use a Random object to generate random integers so your code can roll different numbers on a dice.
"""
import tkinter as tk
from PIL import Image, ImageTk
import random


def get_random_dice_image():
    random_image = None

    rand_num = random.randint(1, 6)

    if rand_num == 1:
        random_image = create_image('dice 1.png', 400, 400)
    elif rand_num == 2:
        random_image = create_image('dice 1.png', 400, 400)
    elif rand_num == 3:
        random_image = create_image('dice 1.png', 400, 400)
    elif rand_num == 4:
        random_image = create_image('dice 1.png', 400, 400)
    elif rand_num == 5:
        random_image = create_image('dice 1.png', 400, 400)
    elif rand_num == 6:
        random_image = create_image('dice 1.png', 400, 400)
    else:
        print("ERROR: Invalid random number!")

    return random_image


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

        self.images = list()
        self.images.append(create_image('dice 1.png', 400, 400)))
        self.images.append(self.dice_2 = create_image('dice 2.png', 400, 400))
        self.images.append(self.dice_3 = create_image('dice 3.png', 400, 400))
        self.images.append(self.dice_4 = create_image('dice 4.png', 400, 400))
        self.images.append(self.dice_5 = create_image('dice 5.png', 400, 400))
        self.images.append(self.dice_6 = create_image('dice 6.png', 400, 400))
        self.label_image = tk.Label(self, image=self.dice_3)
        self.label_image.pack()

        self.button = tk.Button(self, text='Roll!', command=self.on_button_press)
        self.button.pack()

    def on_button_press(self):
        self.label_image.config(image=get_random_dice_image())


if __name__ == '__main__':
    # Create a new object of the class
    app = DiceRoll()
    app.title('My First Python App')

    # Sets the size of the app window
    app.geometry('500x500')

    app.mainloop()

# TODO Generate a random number between 1 and 6 (both 1 and 6 included).
# Change the code to display the dice image to match the number each time the "CLICK HERE TO ROLL" button is pressed.
# Test your code to make sure all 6 sides are displayed.
