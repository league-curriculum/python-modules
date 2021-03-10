import tkinter as tk
from tkinter import simpledialog, Tk
from PIL import Image, ImageTk
from playsound import playsound


def animals():
    window = Tk()
    window.withdraw()

    # TODO 1. Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.

    # TODO 2. Make it so that the user can keep entering new animals.

    # TODO 3. If the user enters 'exit', stop the program


# ======================= DO NOT EDIT THE CODE BELOW =========================

def show_image(filename=None):
    try:
        image = Image.open(filename)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)
        return

    # Use Toplevel since a tk window is already being used for the
    # simpledialog
    screen = tk.Toplevel()
    image = ImageTk.PhotoImage(image)
    tk.Label(master=screen, image=image).pack()
    screen.mainloop()


def moo():
    show_image('cow.jpg')
    playsound('moo.wav')


def quack():
    show_image('duck.jpg')
    playsound('quack.wav')


def woof():
    show_image('dog.jpg')
    playsound('woof.wav')


def meow():
    show_image('cat.jpg')
    playsound('meow.wav')


def llama_scream():
    show_image('llama.jpg')
    playsound('llama.wav')


if __name__ == '__main__':
    animals()
