"""
Objective: Create a program that races a dot across
           the screen when the mouse is pressed
"""

# 1. Create a variable named x and set it to 50
x = 50

def setup():
    size(800, 200)

def draw():
    background(200, 200, 200)
    global x

    # 2. Draw an ellipse of height and width 50. Make sure to use the x variable
    # for its X position. Pick a y value that places it half way down the window.
    fill(0, 0, 255)
    ellipse(x, height/2, 50, 50)
    # 3. Fill in the ellipse with a nice color. Remember to put it above the code
    # where you draw the ellipse.

    # 4. If the mouse is pressed change the x value so that the dot moves to the right
    if mousePressed:
        x += 5

    # 5. If your dot moves slowly, make it move faster. If it moves too quickly,
    # slow it down (you have to figure out what part of your code to change)

    # 6. Use an if statement to display a message when your dot crosses the
    # finish line
    if x > width:
        finish()

def finish():
    fill(0)
    textSize(36)
    text("WINNER!!", width / 2, height / 2)


if __name__ == '__main__':
    if False:
        from ..libraries.Processing3 import *

    try:
        __papplet__
    except NameError:
        import subprocess
        subprocess.call('java -jar ../libraries/processing-py.jar ' + __file__)
