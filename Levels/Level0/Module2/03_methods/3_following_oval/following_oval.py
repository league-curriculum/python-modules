import tkinter as tk

# Tkinter setup
root = tk.Tk()
root.title("Processing Demo")

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()


# Draw function
def draw():
    canvas.delete("all")  # Clear canvas

    # Draw blue ellipse that follows the mouse
    canvas.create_oval(
        mouse_x - 50, mouse_y - 50, mouse_x + 50, mouse_y + 50, fill="blue"
    )

    # Draw red ellipse if mouse is pressed
    if mouse_pressed:
        canvas.create_oval(
            mouse_x - 50, mouse_y - 50, mouse_x + 50, mouse_y + 50, fill="red"
        )

    # Update loop
    canvas.after(10, draw)


# Mouse event handlers
def on_mouse_move(event):
    global mouse_x, mouse_y
    mouse_x, mouse_y = event.x, event.y


def on_mouse_press(event):
    global mouse_pressed
    mouse_pressed = True


def on_mouse_release(event):
    global mouse_pressed
    mouse_pressed = False


# Initialize mouse variables
mouse_x, mouse_y = 0, 0
mouse_pressed = False

# Bind mouse events
canvas.bind("<Motion>", on_mouse_move)
canvas.bind("<ButtonPress-1>", on_mouse_press)
canvas.bind("<ButtonRelease-1>", on_mouse_release)

# Start the draw loop
draw()

# Run the Tkinter event loop
root.mainloop()
