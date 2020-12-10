from playsound import playsound
from PIL import Image

def animals():
    # TODO 1.Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.

    # TODO 2. Make it so that the user can keep entering new animals.

    # Figure out why I need to return to stop indexing error
    return

def moo():
    playsound('cow.wav')
    im = Image.open("sample-image.png")
    im.show()

def quack():
    playsound('duck.wav')
    im = Image.open("sample-image.png")
    im.show()

def woof():
    playsound('dog.wav')
    im = Image.open("sample-image.png")
    im.show()

def meow():
    playsound('meow.wav')
    im = Image.open("sample-image.png")
    im.show()


def llamascream():
    playsound('llama.wav')
    im = Image.open("sample-image.png")
    im.show()


if __name__ == '__main__':

    # Figure out playsound runtime error
    playsound('llama.wav')
    # Figure out showing image
    im = Image.open("sample-image.png")
    im.show()