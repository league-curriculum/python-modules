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

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

def screenClicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))
    
    # 4. Show your moustache by calling the .showturtle() function
    # moustache.showturtle()
    
    # 5. Move your moustache to a new location using .goto(x, y)

if __name__ == '__main__':
    window = turtle.Screen()
    
    # 1. Find an image of a face online that you want to put a moustache on and
    #    add the file to the folder with your code in _01_drawing_ 
    
    # 2. Call the setBackground() function with the image filename inside of the parenthesis
    # setBackground('emoji.png')
    
    # 3. Create a variable called moustache and set it equal to addMoustache('moustache1.gif')
    # moustache = addMoustache('moustache1.gif')

# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screenClicked)
    turtle.done()
