# {{ title }}

Tina is a Turtle that you control with code.  Press run to see what this program does, and see if you can figure out what line tells Tina to say,`"Why, hello there!"`

{{ trinket("meet_tina.py", width="100%", height="600", embed_type="python") | safe }}

Don't worry if you don't understand all of the code.  You don't have to to get started, and more and more of it will become familiar to you as you keep going.

As we saw in the last example, Tina can move!  When she moves, she draws a line.  She can move `forward` and `backward` and turn `right` or `left` a certain number of degrees.

Run this example to see her move:

{{ trinket("move_tina.py", width="100%", height="600", embed_type="python") | safe }}

Turtles like Tina have a pen that draws when they move.  We can tell them to pick the pen up, so that they can move without drawing a line.  Then we can tell them to put the pen down, and they'll draw again.  We tell them this with the `penup()` and `pendown()` commands.

{{ trinket("tinas_pen.py", width="100%", height="600", embed_type="python") | safe }}


Thanks to [Tinket](https://trinket.io/) for the original Tina code. 