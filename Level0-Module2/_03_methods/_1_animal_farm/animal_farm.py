from tkinter import simpledialog, Tk

from playsound import playsound
from PIL import Image


def animals():
    window = Tk()
    window.withdraw()

    # TODO 1.Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.

    # TODO 2. Make it so that the user can keep entering new animals.


def moo():
    im = Image.open("cow.jpg")
    im.show()
    playsound('moo.wav')


def quack():
    im = Image.open("duck.jpg")
    im.show()
    playsound('quack.wav')


def woof():
    im = Image.open("dog.jpg")
    im.show()
    playsound('woof.wav')


def meow():
    im = Image.open("cat.jpg")
    im.show()
    playsound('meow.wav')


def llama_scream():
    im = Image.open("llama.jpg")
    im.show()
    playsound('llama.wav')


if __name__ == '__main__':
    animals()
