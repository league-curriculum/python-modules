# First up, we need to get turtle into the game. It's like summoning your drawing buddy.
import turtle

# Let's make a turtle and name it Tina because why not? Tina's going to be our artist.
tina = turtle.Turtle()

# Making Tina look like a turtle because, honestly, it's just more fun that way.
tina.shape("turtle")

# Before we draw, let’s get Tina to the center. This is where we’ll start our masterpiece.
tina.penup()  # Picking up the pen so we don't draw anything while moving to the starting point.
tina.goto(
    0, -100
)  # Moving to the spot. We’re starting at the bottom of the big circle.
tina.pendown()  # Now we’re ready to draw.

# Time for the big red circle. It’s the outermost part of our target.
tina.color("red")  # Changing Tina's pen to red.
tina.begin_fill()  # We're filling this circle with color, so let’s start that.
tina.circle(100)  # This tells Tina to draw a circle with a radius of 100.
tina.end_fill()  # Done with the red circle.

# Now, let’s go for the smaller white circle inside the red one.
tina.penup()  # Gotta lift the pen before moving.
tina.goto(0, -80)  # Adjusting the position for the white circle.
tina.pendown()  # And we draw again.
tina.color("white")  # Switching to white color now.
tina.begin_fill()
tina.circle(80)  # Smaller circle, so a radius of 80 this time.
tina.end_fill()

# Finally, the smallest circle, the bullseye, in black.
tina.penup()  # Up with the pen again.
tina.goto(0, -60)  # Getting in position for the final circle.
tina.pendown()  # Down goes the pen.
tina.color("black")  # The color for our bullseye.
tina.begin_fill()
tina.circle(60)  # The smallest circle, so it’s got a radius of 60.
tina.end_fill()

# And that’s it! We’ve got ourselves a target. Time to admire our work.
turtle.mainloop()  # This keeps the window open so we can actually see what we’ve done.
