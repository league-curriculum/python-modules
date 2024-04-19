#  COMBINED ALL THREE FILES INTO ONE FILE AND REMOVED THE .PYDE FILE.  THIS CODE STILL NEEDS INSTRUCTIONAL COMMENTS ADDED TO IT BUT THE CODE IS COMPLETE.
#
import tkinter as tk
import math

"""
This module contains classes for a Pong game and functionality to run the game in a Tkinter GUI.

Classes:
    Ball: Represents the ball in the Pong game.
    Paddle: Represents the paddle in the Pong game.

Functions:
    setup(): Sets up the initial game state.
    draw(canvas): Handles the game loop and updates the game state.
    keyPressed(event): Handles keyboard input for moving the paddle.
    keyReleased(event): Stops the paddle movement when the key is released.
"""


class Ball:
    """
    Represents the ball in the Pong game.

    Attributes:
        x (float): The x-coordinate of the ball.
        y (float): The y-coordinate of the ball.
        speed (float): The speed of the ball.
        radius (float): The radius of the ball.
        x_speed (float): The horizontal speed of the ball.
        y_speed (float): The vertical speed of the ball.
        currently_intersects (bool): Flag indicating if the ball is currently intersecting with the paddle.

    Methods:
        update(): Updates the position of the ball.
        draw(canvas): Draws the ball on the canvas.
        collision(paddle): Checks for collision with the paddle and updates the ball's direction if necessary.
    """

    def __init__(self, x=0, y=0, ball_speed=5, radius=20):
        """
        Initializes a Ball object.

        Args:
            x (float, optional): The initial x-coordinate of the ball. Defaults to 0.
            y (float, optional): The initial y-coordinate of the ball. Defaults to 0.
            ball_speed (float, optional): The initial speed of the ball. Defaults to 5.
            radius (float, optional): The radius of the ball. Defaults to 20.
        """
        self.x = x
        self.y = y
        self.speed = ball_speed
        self.radius = radius
        self.x_speed = self.speed
        self.y_speed = self.speed
        self.currently_intersects = False

    def update(self):
        """
        Updates the position of the ball based on its speed and handles wall collisions.
        """
        if self.x + self.radius > canvas_width or self.x - self.radius < 0:
            self.x_speed = -self.x_speed
        if self.y + self.radius < 0:
            self.y_speed = -self.y_speed

        self.x += self.x_speed
        self.y += self.y_speed

    def draw(self, canvas):
        """
        Draws the ball on the canvas.

        Args:
            canvas (tk.Canvas): The canvas to draw the ball on.
        """
        canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
            fill="white",
            outline="",
        )

    def collision(self, paddle):
        """
        Checks for collision with the paddle and updates the ball's direction if necessary.

        Args:
            paddle (Paddle): The paddle object to check for collision.
        """
        side = None
        edge_x = self.x
        edge_y = self.y

        if self.x < paddle.x:
            edge_x = paddle.x  # Ball is left of the paddle
            side = "left"
        elif self.x > paddle.x + paddle.width:
            edge_x = paddle.x + paddle.width  # Ball is right of the paddle
            side = "right"

        if self.y < paddle.y:
            edge_y = paddle.y  # Ball is above the paddle
            side = "top"
        elif self.y > paddle.y + paddle.height:
            edge_y = paddle.y + paddle.height  # Ball is below the paddle
            side = "bottom"

        # Get distance from Pythagorean theorem
        dist_x = self.x - edge_x
        dist_y = self.y - edge_y
        distance = math.sqrt((dist_x * dist_x) + (dist_y * dist_y))

        # If the distance is less than the radius, collision!
        if distance <= self.radius:
            if not self.currently_intersects:
                self.currently_intersects = True
            if side == "right" or side == "left":
                self.x_speed = -self.x_speed
            else:
                self.y_speed = -self.y_speed
        else:
            # Sometimes upon first collision the ball would still be within
            # the paddle, causing the ball to rebound back and forth.
            # Resetting the variable here ensures there's only 1 change of
            # direction until the ball and paddle no longer intersect.
            self.currently_intersects = False


class Paddle:
    """
    Represents the paddle in the Pong game.

    Attributes:
        x (float): The x-coordinate of the paddle.
        y (float): The y-coordinate of the paddle.
        width (float): The width of the paddle.
        height (float): The height of the paddle.
        x_speed (float): The horizontal speed of the paddle.

    Methods:
        update(): Updates the position of the paddle based on its speed.
        draw(canvas): Draws the paddle on the canvas.
    """

    def __init__(self, x, y=None, paddle_width=100, paddle_height=20):
        """
        Initializes a Paddle object.

        Args:
            x (float): The initial x-coordinate of the paddle.
            y (float, optional): The initial y-coordinate of the paddle. If not provided, it defaults to the bottom of the screen.
            paddle_width (float, optional): The width of the paddle. Defaults to 100.
            paddle_height (float, optional): The height of the paddle. Defaults to 20.
        """
        self.x = x
        self.y = canvas_height - paddle_height if y is None else y
        self.width = paddle_width
        self.height = paddle_height
        self.x_speed = 0

    def update(self):
        """
        Updates the position of the paddle based on its speed, ensuring it stays within the screen bounds.
        """
        if (self.x + self.x_speed >= 0) and (
            self.x + self.x_speed <= canvas_width - self.width
        ):
            self.x += self.x_speed

    def draw(self, canvas):
        """
        Draws the paddle on the canvas.

        Args:
            canvas (tk.Canvas): The canvas to draw the paddle on.
        """
        canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height,
            fill="white",
            outline="",
        )


# Global variables
ball = None
paddle = None
canvas_width = 800
canvas_height = 600
root = None
canvas = None
game_running = False


def setup():
    """
    Sets up the initial game state.
    """
    global ball, paddle, root, canvas

    # Create the Tkinter root window
    root = tk.Tk()
    root.title("Pong Game")

    # Create the canvas
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
    canvas.pack()

    # Create buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    play_button = tk.Button(button_frame, text="Play Game", command=start_game)
    play_button.pack(side=tk.LEFT, padx=10)

    quit_button = tk.Button(button_frame, text="Quit Game", command=quit_game)
    quit_button.pack(side=tk.LEFT, padx=10)

    # Bind keyboard events
    root.bind("<KeyPress>", keyPressed)
    root.bind("<KeyRelease>", keyReleased)

    # Start the Tkinter event loop
    root.mainloop()


def draw_game():
    """
    Handles the game loop and updates the game state.
    """
    global ball, paddle, canvas, game_running

    if game_running:
        # Clear the canvas
        canvas.delete("all")

        # Update and draw the ball
        ball.update()
        ball.draw(canvas)

        # Update and draw the paddle
        paddle.update()
        paddle.draw(canvas)

        # Call the ball object's collision() method and pass the paddle object as an input variable.
        ball.collision(paddle)

        # End the game when the ball goes below the bottom of the screen.
        if ball.y > canvas_height:
            canvas.create_text(
                canvas_width / 2,
                canvas_height / 2,
                text="Game Over",
                fill="white",
                font=("Arial", 24),
            )
            game_running = False
        else:
            # Schedule the next frame
            root.after(10, draw_game)


def keyPressed(event):
    """
    Handles keyboard input for moving the paddle.
    """
    global paddle
    if event.keysym == "Left":
        paddle.x_speed = -10
    elif event.keysym == "Right":
        paddle.x_speed = 10


def keyReleased(event):
    """
    Stops the paddle movement when the key is released.
    """
    global paddle
    if event.keysym in ("Left", "Right"):
        paddle.x_speed = 0


def start_game():
    """
    Starts the game loop.
    """
    global ball, paddle, game_running

    # Initialize your ball variable to a new Ball(), for example:
    ball = Ball(canvas_width / 2, 0)

    # Initialize your paddle variable to a new Paddle() for example:
    paddle = Paddle(canvas_width / 2 - 50)

    game_running = True
    draw_game()


def quit_game():
    """
    Quits the application.
    """
    root.quit()


# Setup the initial state
setup()
