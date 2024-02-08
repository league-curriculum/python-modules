import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.penup()
tina.write("I start at 0, 0")

tina.goto(100,100)
tina.write("This is 100, 100")

tina.goto(-100,-100)
tina.write("This is -100, -100")

tina.goto(100,-100)
tina.write("This is 100, -100")

tina.goto(-100,100)
tina.write("This is -100, 100")

tina.goto(-100, 0)