import turtle
import random
from PIL import Image


class Turkey:
    window = None
    image_width = 150
    image_height = 109

    def __init__(self, x, y, filename='turkey.gif', name=None):
        self.x = x;
        self.y = y - (Turkey.image_height / 4)
        self.name = name
        self.size = 100;
        self.min_speed = 5;
        self.max_speed = 15;
        self.image = Image.open(filename)

        if Turkey.window is not None:
            Turkey.window.addshape(filename)

        self.turtle_object = turtle.Turtle()
        self.turtle_object.hideturtle()
        self.turtle_object.shape(filename)
        self.turtle_object.penup()
        self.turtle_object.speed(0)
        self.turtle_object.goto(self.x, self.y)
        self.turtle_object.showturtle()

    def check_finish(self):
        return self.x > (Turkey.window.window_width() / 2)

    def trot(self):
        self.x += random.randint(self.min_speed, self.max_speed)
        self.turtle_object.goto(self.x, self.y)

    def winner(self):
        self.turtle_object.hideturtle()
        self.turtle_object.backward(450)
        self.turtle_object.showturtle()
        win_message = 'Winner!!!' if self.name is None else self.name + " is the Winner!!!"
        self.turtle_object.write(arg=win_message, move=True, align='left', font=('Arial', 24, 'normal'))
