import turtle
from PIL import Image

def setBackground(filename):
    
    try:
        image = Image.open(filename)
    except:
        print( "ERROR: Unable to find file " + filename )
        return
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(filename)

def addMoustache(filename):
    m = turtle.Turtle()
    
    m.hideturtle()
    window.addshape(filename)
    m.shape(filename)
    m.penup()
    m.speed(0)
    
    return m

def screenClicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))
    moustache.showturtle()
    
    # 4. Move the turtle to a new location using .goto()
    moustache.goto(x, y)

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    
    # 1. Find an image of a face online that you want to put a moustache on and
    #    add the file to the folder with your code in _01_drawing_ 
    
    # 2. Create a variable to hold the filename of the background as a string,
    #    for example, bgImage = 'emoji.gif'
    bgImage = 'emoji.png'
    
    # 3. Call the setBackground() function with your variable inside of the parenthesis
    #    for example, setBackground(bgImage)
    setBackground(bgImage)
    
    # 4. Create a variable to hold the filename of the mousetache image as a string
    moustacheImage = 'moustache1.gif'
    
    # 5. Call the addMoustache function with your moustache variable
    moustache = addMoustache(moustacheImage)

# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screenClicked)
    turtle.done()
