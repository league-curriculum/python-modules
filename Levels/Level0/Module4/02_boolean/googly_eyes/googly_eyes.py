####################################################
# This code still neeed to be completed
###################################################


from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk
import os


class GooglyEyes:
    def __init__(self, master):
        self.master = master
        self.master.title("Googly Eyes")

        # Load image and adjust canvas size
        self.face = self.load_image("big_eye_bird.png", (750, 600))
        self.canvas = Canvas(master, width=self.face.width(), height=self.face.height())
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.face)

        # Define eye positions and sizes relative to image size
        self.left_eye_x, self.left_eye_y = 240, 212
        self.right_eye_x, self.right_eye_y = 520, 212
        self.eye_radius = 140

        # Draw initial pupils and store references
        self.left_eye_pupil = self.draw_eye(
            self.left_eye_x, self.left_eye_y, self.eye_radius, "left"
        )
        self.right_eye_pupil = self.draw_eye(
            self.right_eye_x, self.right_eye_y, self.eye_radius, "right"
        )

        # Bind mouse click event to move_eye function
        self.canvas.bind("<Button-1>", self.move_eye)

    def load_image(self, file, size):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, file)
        image = Image.open(image_path)
        image = image.resize(size, resample=Image.BILINEAR)  # Adjust image size
        return ImageTk.PhotoImage(image)

    def draw_eye(self, eye_center_x, eye_center_y, eye_radius, side):
        # Calculate pupil positions
        if side == "left":
            pupil_x, pupil_y = eye_center_x - eye_radius, eye_center_y
        else:
            pupil_x, pupil_y = eye_center_x + eye_radius, eye_center_y

        # Draw pupil
        pupil = self.canvas.create_oval(
            pupil_x - 15, pupil_y - 15, pupil_x + 15, pupil_y + 15, fill="black"
        )
        return pupil

    def move_eye(self, event):
        # Move left pupil
        self.canvas.coords(
            self.left_eye_pupil, event.x - 15, event.y - 15, event.x + 15, event.y + 15
        )

        # Move right pupil
        self.canvas.coords(
            self.right_eye_pupil, event.x - 15, event.y - 15, event.x + 15, event.y + 15
        )


root = Tk()
app = GooglyEyes(root)
root.mainloop()
