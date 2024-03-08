import tkinter as tk
import os
import simpleaudio as sa


# Function to load audio file
def get_audio_file(file):
    file_path = os.path.join(os.path.dirname(__file__), file)
    return sa.WaveObject.from_wave_file(file_path)


# Function to play sound
def play_sound(file):
    audio_file = get_audio_file(file)
    play_obj = audio_file.play()
    play_obj.wait_done()


# Mouse event handlers
def on_mouse_press(event):
    canvas.data["mouse_pressed"] = True


def on_mouse_release(event):
    canvas.data["mouse_pressed"] = False


# Main loop
def setup():
    canvas.data["x"] = 50
    canvas.data["sound_played"] = False


def draw():
    canvas.delete("all")
    canvas.create_oval(canvas.data["x"], 50, canvas.data["x"] + 50, 150, fill="red")

    # Move the ellipse to the right if the mouse is pressed
    if canvas.data["mouse_pressed"]:
        canvas.data["x"] += 10

    # Play sound when the ellipse crosses the finish line
    if canvas.data["x"] >= 800 and not canvas.data["sound_played"]:
        play_sound("ding.wav")
        canvas.data["sound_played"] = True

    root.after(50, draw)


# Tkinter setup
root = tk.Tk()
root.title("Ellipse Traveler")

canvas = tk.Canvas(root, width=800, height=200, bg="white")
canvas.pack()

# Initialize canvas data
canvas.data = {}
canvas.data["mouse_pressed"] = False

# Bind mouse events
canvas.bind("<ButtonPress-1>", on_mouse_press)
canvas.bind("<ButtonRelease-1>", on_mouse_release)

# Start the main loop
setup()
draw()

# Run the Tkinter event loop
root.mainloop()
