import turtle
from PIL import Image

# ================= Instructions at the bottom of this file ===================


def set_background(filename):
    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return

    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(filename)


def add_moustache(filename):
    m = turtle.Turtle()

    m.hideturtle()
    window.addshape(filename)
    m.shape(filename)
    m.penup()
    m.speed(0)

    return m


# ====================== DO NOT EDIT THE CODE ABOVE ===========================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))

    # 4. Show your moustache by calling the .showturtle() function
    # moustache.showturtle()

    # 5. Move your moustache to a new location using .goto(x, y)


if __name__ == '__main__':
    window = turtle.Screen()

    # 1. Find an image of a face online that you want to put a moustache on and
    #    add the file to the folder with your code

    # 2. Call the set_background() function with the image filename inside of the parenthesis
    set_background('emoji.png')

    # 3. Create a variable called moustache and set it equal to add_moustache('moustache1.gif')
    # moustache = add_moustache('moustache1.gif')

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screen_clicked)
    turtle.done()
