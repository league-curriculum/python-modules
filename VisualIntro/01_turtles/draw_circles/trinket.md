# Drawing Circles

## What Can Tina Do?

Let's review what Tina can do with the commands that we've seen so far: 

This code creates a turtle and names her "Tina":

```python
import turtle
tina = turtle.Turtle()
```

We can tell Tina to move forward or backward:

```python
tina.forward(20)
tina.backward(15)
```

We can tell Tina to turn left or right, which changes the direction that Tina moves when 
she moved forward or backward:
```python
tina.left(90)
tina.right(90)
```

We can tell Tina to go to a place on the screen:
```python 
tina.goto(0,0)
tina.goto(100,100)
```

When telling her to `goto`, remember that the first number is the left-right position, and
goes from -200 ( on the left ) to 200 ( on the right) . The second number is the top-bottom position, and goes from -200 (top) to -200 ( bottom ). That means that (0,0) is right in the middle. 

We can tell Tina to pick up her pen and not draw, or put her pen down to draw a line:
```python
tina.penup()
tina.pendown()
```

We can change the color of the pen
```python
tina.color('blue')
```

We can tell tina to draw a circle of a specific size (radius):
```python 
tina.circle(50)
```

We can tell tina to fill in a circle, instead of just drawing the outside line: 
```python
tina.begin_fill() 
tina.circle(100) 
tina.end_fill()  
```

::: tip
If you want to try something more advanced, you can [read the documentation for the turtle module](https://docs.python.org/3/library/turtle.html#module-turtle) to find many more things you can tell Tina to do. 
:::

## An Example of Circles

Let's put all these commands together to draw a face. 

{{ trinket("drawing_circles_example.py", width="100%", height="600", embed_type="python") | safe }}


## Draw Your Own Circles

Now it is your turn! Use what you have learned so far to draw your own shapes. 

{{ trinket("drawing_circles.py", width="100%", height="600", embed_type="python") | safe }}



