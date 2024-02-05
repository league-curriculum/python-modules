import turtle
from PIL import Image
import os


# Do not change this function
def setBackground(filename):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory, filename)

    try:
        image = Image.open(file_path)
    except:
        print("ERROR: Unable to find file " + file_path)
        return

    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(file_path)


# Do not change this function
def addMoustache(filename):
    m = turtle.Turtle()
    m.hideturtle()

    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory, filename)

    try:
        window.addshape(file_path)
    except turtle.TurtleGraphicsError:
        print("ERROR: Unable to find file " + file_path)
        return

    m.shape(file_path)
    m.penup()
    m.speed(0)

    return m


# Only add the code from step 4 to this function
def screenClicked(x, y):
    print("You pressed: x=" + str(x) + ", y=" + str(y))
    moustache.showturtle()

    # 4. Move the turtle to a new location using .goto()
    moustache.goto(x, y)  # ;


# ====================== DO NOT EDIT THE CODE ABOVE ===========================
window = turtle.Screen()


# 1. Find an image of a face online that you want to put a moustache on and
#    add the file to the folder with your code in 01_drawing_

# 2. Create a variable to hold the filename of the background as a string,
#    for example, bgImage = 'emoji.gif'
bgImage = "emoji.png"  # ;

# 3. Call the setBackground() function with your variable inside of the parenthesis
#    for example, setBackground(bgImage)
setBackground(bgImage)  # ;

# 4. Create a variable to hold the filename of the moustache image as a string
moustacheImage = "moustache1.gif"  # ;

# 5. Call the addMoustache function with your moustache variable
moustache = addMoustache(moustacheImage)  # ;

# ===================== DO NOT EDIT THE CODE BELOW ============================
window.onclick(screenClicked)
turtle.done()
