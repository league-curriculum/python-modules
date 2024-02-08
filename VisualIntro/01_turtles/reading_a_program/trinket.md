# Reading A Program

Let's look at our first program again and study it a bit more.  

{{ trinket("meet_tina.py", width="100%", height="300", embed_type="python") | safe }}

There are a lot of interesting parts to this program, and it is important to know what they are. One of the ways that programmers explain their programs
is with comments. In Python, a comment is everything on a line that comes after
a hash mark, `#`. 

```python
# tell Tina to pick her pen up
tina.penup()
```

Comments are for people to read; the computer ignores them. Let's
look a our first program one more time, but this time with comments: 

```python
# The import statement tells python that we want to use the turtle module.
# a module is a collection of code that is stored in a file.
import turtle

# The first 'turtle' is the name of the module, and the second 'Turtle'
# is another group of code cladded a 'class'. The 'Turtle' class has code
# that allows us to create a turtle
#
# The equals sign means that we are giving the turtle a name, 'tina'.
tina = turtle.Turtle()

# the '.shape' part of this line is called a method, sometimes known as a function.
# This method tells the turtle what shape to have. The 'tina.shape' part
# means that we want to change the shape of tina.
tina.shape('turtle')

# Read the following lines and see if you can figure out what they do.
tina.penup()
tina.forward(20)
tina.write("Why, hello there!")
tina.backward(20)
```

Now we know what the lines that start with `#` are called, but what are the
other lines called? Those lines are called "statements". There are many other
names we have for lines of code, which we wil learn as we go along. 
