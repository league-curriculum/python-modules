import turtle

if __name__ == '__main__':
    my_turtle = turtle.Turtle()
    my_turtle.speed(100)

    # TODO 1) Set the X position of the turtle so that it starts on the left.
    x = -400
    my_turtle.penup()
    my_turtle.setx(x)
    my_turtle.pendown()
    # TODO 2) Make the turtle draw a star shape. Hint: angle=144.
    for i in range(10):
        for j in range(5):
            my_turtle.forward(30)
            my_turtle.right(144)
        my_turtle.penup()
        x += 50
        my_turtle.setx(x)
        my_turtle.pendown()

    # TODO 3) Set the length of each line in the star to 30

    # TODO: CHALLENGE
    #       Make the robot draw a line of stars like this:
    #       http://bit.ly/RobotWalk
    #       Hint: The distance between stars is 50.

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()