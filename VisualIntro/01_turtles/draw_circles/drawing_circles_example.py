import turtle
tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(1000)


# Move to draw the face
tina.penup()
tina.goto(30,-150)
tina.pendown()

# Draw a green face
tina.color('green')
tina.begin_fill()
tina.circle(130)
tina.end_fill()

# Move to the left eye
tina.penup()
tina.goto(0,0)
tina.pendown()

# Draw the left eye
# Left eye sclera
tina.color('white')
tina.begin_fill()
tina.circle(20)
tina.end_fill()

# Left eye pupil
tina.color('black')
tina.begin_fill()
tina.circle(10)
tina.end_fill()

# Move to the right eye
tina.penup()
tina.forward(60)
tina.right(45) # Turn a bit to make the eye tilted
tina.pendown()

# Draw the right eye
# Right eye sclera
tina.color('white')
tina.begin_fill()
tina.circle(30)
tina.end_fill()

# Right eye pupil
tina.color('black')
tina.begin_fill()
tina.circle(10)
tina.end_fill()

# Move to the mouth
tina.penup()
tina.right(90)
tina.forward(90)
tina.pendown()

# Draw the mouth
tina.color('maroon')
tina.begin_fill()
tina.circle(40)
tina.end_fill()

tina.penup()
tina.goto(25,-25)