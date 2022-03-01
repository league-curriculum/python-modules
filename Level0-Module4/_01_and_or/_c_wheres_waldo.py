"""
Make a program where the user has to find Waldo!
"""

# =========== SOUND =================
# Some computers are unable to play sounds.
# If you cannot play sound on this computer, set canPlaySounds to false.
# If you are not sure, ask your teacher
can_play_sounds = False

IMAGES_PATH = '../images/'
waldo = None

def setup():
    # Find a Where's Waldo picture and drop it onto the sketch.

    # Use the size() function to set the width and height of your sketch

    # Change the line below to match your file name.
    global waldo
    waldo = loadImage(IMAGES_PATH + "waldo.jpg")

    # Resize your waldo picture to the same size as the sketch

    pass

def draw():
    # Use the background() function to make the waldo image your
    # sketch background

    # If the user presses the mouse...
    # *Hint* use the mousePressed variable

    # Use this print statement to help you find the location
    # of Waldo to use in the code below

    # Check if the location of the mouse is anywhere on the image of Waldo.
    # If it is, print “Waldo found!”  Use the text() command to write it
    # on the sketch.

    # Use the play_woohoo() method below.

    # However, if the mouse is not on Waldo, print "Not here!"
    # Use the text() command to write it on the sketch.

    # Use the play_doh() method below.

    pass


# =================== This code is needed to play sounds. ===================
woohoo = None
doh = None

if can_play_sounds:
    add_library('sound')

def play_woohoo():
    textSize(36)
    fill(0, 0, 255)
    text("WOO HOO!", mouseX - 72, mouseY)

    global woohoo
    if can_play_sounds:
        if woohoo is None:
            woohoo = SoundFile(this, "homer-woohoo.wav")
        woohoo.stop()
        woohoo.play()


def play_doh():
    textSize(36)
    fill(255, 0, 0)
    text("DOH!", mouseX - 36, mouseY)

    global doh
    if can_play_sounds:
        if doh is None:
            doh = SoundFile(this, "homer-doh.wav")
        doh.stop()
        doh.play()


if __name__ == '__main__':
    if False:
        from ..libraries.Processing3 import *

    try:
        __papplet__
    except NameError:
        import subprocess
        subprocess.call('java -jar ../libraries/processing-py.jar ' + __file__)
