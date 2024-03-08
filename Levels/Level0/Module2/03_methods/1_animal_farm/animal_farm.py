from tkinter import simpledialog, Tk
import os
import simpleaudio as sa

# If simpleaudio is not installed, you can install it by running the following command in the terminal
# pip install simpleaudio
from PIL import Image


def animals():
    window = Tk()
    window.withdraw()

    # TODO 1. Create a variable for how many animals the user wants to see
    num_animals = 3  # ;
    # TODO 2. Add the variable from step 1 to the range function
    for i in range(num_animals):
        # TODO 3.Ask the user which animal they want, then see and
        #  hear the animal they chose using one of the methods below.
        animal = simpledialog.askstring(
            title="Question", prompt="Which animal do you want?"  # ;
        )
        if animal == "cow":
            moo()
        elif animal == "duck":
            quack()
        elif animal == "dog":
            woof()
        elif animal == "cat":
            meow()
        else:
            llamascream()

    # TODO 4. Make it so that the user can keep entering new animals. Hint: use a while loop instead of a for loop.


# DO NOT MODIFY THE CODE BELOW!!!


def get_audio_file(file):
    file_path = os.path.join(os.path.dirname(__file__), file)
    return sa.WaveObject.from_wave_file(file_path)


def get_image_file(file):
    file_path = os.path.join(os.path.dirname(__file__), file)
    return Image.open(file_path)


def moo():
    im = get_image_file("cow.jpg")
    im.show()
    get_audio_file("moo.wav").play()


def quack():
    im = get_image_file("duck.jpg")
    im.show()
    get_audio_file("quack.wav").play()


def woof():
    im = get_image_file("dog.jpg")
    im.show()
    get_audio_file("woof.wav").play()


def meow():
    im = get_image_file("cat.jpg")
    im.show()
    get_audio_file("meow.wav").play()


def llamascream():
    im = get_image_file("llama.jpg")
    im.show()
    get_audio_file("llama.wav").play()


animals()
