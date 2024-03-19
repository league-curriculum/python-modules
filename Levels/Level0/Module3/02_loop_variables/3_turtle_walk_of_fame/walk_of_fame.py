import turtle  # ;

# TODO START: Import turtle.  Then create a turtle and set the shape to "turtle" and the color to "blue" and "green". Set the speed to 100.
my_turtle = turtle.Turtle()  # ;
my_turtle.shape("turtle")  # ;
my_turtle.color("blue", "green")  # ;
my_turtle.speed(100)  # ;

# TODO 1) Call the penup() function to lift the pen up so that the turtle does not draw when it moves.
# TODO 2) Set the X position of the turtle so that it starts on the left use the .setx() function.
my_turtle.penup()  # ;
my_turtle.setx(-200)  # ;


# TODO 2) Create a function called draw_star that will make the turtle draw a star shape. Use the penup() and pendown() functions to move the turtle between stars without drawing. Hint: angle=144.
def draw_star():  # ;
    my_turtle.pendown()  # ;
    for _ in range(5):  # ;
        my_turtle.forward(30)  # ;
        my_turtle.right(144)  # ;
    my_turtle.penup()  # ;
    my_turtle.forward(50)  # ;


# TODO 3) Set the length of each line in the star to 30

# TODO 4) Call draw_star funcion.

for _ in range(5):  # ;
    draw_star()  # ;

# TODO: CHALLENGE
#       Make the turtle draw a line of stars like the image in
#       this folder.
#       Hint: The distance between stars is 50.


# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
