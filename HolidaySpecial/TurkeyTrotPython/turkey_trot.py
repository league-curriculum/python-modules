import turtle
from Turkey import Turkey
from PIL import Image, ImageDraw


def set_background(filename):
    try:
        image = Image.open(filename)
    except FileNotFoundError:
        print("ERROR: Unable to find file " + filename)
        return

    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(filename)


def draw_lane_markers(num_turkeys):
    lane_maker = turtle.Turtle()
    lane_maker.hideturtle()
    lane_maker.shape(None)
    lane_maker.penup()
    lane_maker.speed(0)
    lane_maker.fillcolor('black')

    for i in range(num_turkeys):
        start_height = -(HEIGHT / 2)
        height = start_height + (i * (HEIGHT / num_turkeys))
        lane_maker.goto(-(WIDTH / 2), height)
        lane_maker.setheading(0)
        lane_maker.begin_fill()
        for k in range(2):
            lane_maker.forward(WIDTH)
            lane_maker.left(90)
            lane_maker.forward(10)
            lane_maker.left(90)
        lane_maker.end_fill()


# ===================== DO NOT EDIT THE CODE ABOVE ============================


if __name__ == '__main__':
    race_in_progress = True
    WIDTH = 1150
    HEIGHT = 600

    # 1. Set the window variable to turtle.Screen()
    window = None

    # 2. Call the window's setup() method with the WIDTH and HEIGHT variables

    # 3. Call the set_background() method with 'grass.png'

    # 4. Run your code. You should see a window with an image of grass

    # 5. Set the Turkey.window variable to the window variable created in step 1
    # Turkey.window = window

    # 6. Create and set a variable to hold the number of Turkeys you want
    # in the race from 2 to 7 (7 is recommended)

    # 7. Call the draw_lane_markers function and pass in the number of turkeys

    # 8. Create and set a variable to hold the width of each lane
    # *HINT* the lane width is the HEIGHT of the window divided by the number of
    #        turkeys in the race

    # 9. Create a variable called start_x and set it to -(WIDTH / 2)

    # 10. Create a variable called start_y and set it to (HEIGHT / 2)

    # 11. Create your turkey competitors!
    # gobbler = Turkey(start_x, start_y - (1 * lane_width))
    #
    # *HINT* the (1 * lane_width) part will be different for each turkey

    while race_in_progress:
        pass

        # 12. Call the trot() method for each one of your turkeys!

        # 13. For each turkey, use an 'if' statement and call your turkey's
        # check_finish() method
        # if gobbler.check_finish():

            # 14. If the turkey finished, call that turkey's winner() method,
            # gobbler.winner()

            # 15. set the race_in_progress variable to True

# ===================== DO NOT EDIT THE CODE BELOW ============================

    turtle.done()
