import tkinter as tk


def setup():
    window = tk.Tk()
    window.title("Ellipse Traveler")

    canvas = tk.Canvas(window, width=800, height=200, bg="white")
    canvas.pack()

    # Initialize variables
    x = {"value": 50}
    sound_played = {"value": False}
    can_play_sounds = {"value": False}

    # Bind mouse press event to move the ellipse
    canvas.bind("<ButtonPress-1>", lambda event: on_mouse_press(event, x))

    # Draw the ellipse
    draw(canvas, x, sound_played, can_play_sounds)

    window.mainloop()


# Function to draw the ellipse
def draw(canvas, x, sound_played, can_play_sounds):
    canvas.delete("all")
    canvas.create_oval(x["value"], 75, x["value"] + 50, 125, fill="blue")

    # If the ellipse crosses the finish line, play sound
    if x["value"] >= 750 and not sound_played["value"]:
        play_sound(canvas, sound_played, can_play_sounds)
        sound_played["value"] = True

    # Update loop
    canvas.after(50, draw, canvas, x, sound_played, can_play_sounds)


# Function to play sound
def play_sound(canvas, sound_played, can_play_sounds):
    if can_play_sounds["value"] and not sound_played["value"]:
        # Code to play sound
        pass
    canvas.create_text(400, 100, text="WINNER!!", fill="black", font=("Arial", 36))


# Function to handle mouse press event
# Move the ellipse 10 pixels to the right
# Do not modify this function
def on_mouse_press(event, x):
    x["value"] += 10


# Call the setup function to start the program
setup()  # ;
