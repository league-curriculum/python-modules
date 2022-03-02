"""
Go to the recipe to run the demonstration in Amazing Rings.html before starting
this program
"""


def setup():
    pass
    # Set the size of your sketch to be a rectangle like in the recipe demonstration

    # Call the noFill() command so all the ellipses will be transparent

def draw():
    pass
    # Use a for loop to make the first set of rings that will start in the left half
    # of the window.

    # Make this set of rings move across the sketch to the right
    # Hint: Make two variables, one for x and another for the speed.
    #       Then increase x by the amount in speed.

    # When the rings reach the right side of the sketch, reverse the direction so
    # they move.
    # Hint: speed = -speed */


    # When the rings reach the left side of the sketch, reverse the direction again

    # CHALLENGE - to finish the Amazing Rings

    # Add another for loop to draw the second set of rings that will start in the
    # right half of the window

    # Make this set of rings move in the opposite direction to the other rings
    # These rings must also "bounce" off the sides of the window.

if __name__ == '__main__':
    if False:
        from ...libraries.Processing3 import *

    try:
        __papplet__
    except NameError:
        import subprocess
        subprocess.call('java -jar ../../libraries/processing-py.jar ' + __file__)
