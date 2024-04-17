import tkinter as tk
from tkinter import PhotoImage
import math
import os
from PIL import Image, ImageTk

# 1. Create a variable called face and set it to None.
face = None  # ;


def setup():

    global face
    image_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(image_directory, "big_eye_bird.png")

    # 2. Create a new Image object called image and set it equal to Image.open(image_path).
    image = Image.open(image_path)  # ;
    # 3. Create 2 variables called canvas_width and canvas_height and set them to 750 and 800 respectively.
    canvas_width = 750  # ;
    canvas_height = 800  # ;
    # 4. Resize the image to fit the canvas by calling the thumbnail method on the image object. Pass in a tuple with the canvas_width and canvas_height as the first argument and Image.LANCZOS as the second argument. Set the result to the face variable.
    image.thumbnail((canvas_width, canvas_height), resample=Image.LANCZOS)  # ;
    # 5. Create a new PhotoImage object called face and set it equal to ImageTk.PhotoImage(image).
    face = ImageTk.PhotoImage(image)  # ;

    # The below code is used to display the image on the canvas.
    # Do not modify it.
    root.geometry(f"{canvas_width}x{canvas_height}")
    canvas.configure(width=canvas_width, height=canvas_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=face)


def draw(event):

    global face
    canvas.create_image(0, 0, anchor=tk.NW, image=face)

    # 6. Create 5 variables called left_eye_x, left_eye_y, right_eye_x, right_eye_y, and eye_radius. Set them to 240, 212, 520, 265, and 280/2 respectively.
    left_eye_x = 240  # ;
    left_eye_y = 212  # ;
    right_eye_x = 520  # ;
    right_eye_y = 265  # ;
    eye_radius = 280 / 2  # ;

    # 7. Create a white oval for the left eye using the canvas.create_oval method on the canvas object. Pass in the left_eye_x - eye_radius, left_eye_y - eye_radius, left_eye_x + eye_radius, left_eye_y + eye_radius as the first 4 arguments. Set fill to "white" and outline to an empty string.
    canvas.create_oval(  # ;
        left_eye_x - eye_radius,  # ;
        left_eye_y - eye_radius,  # ;
        left_eye_x + eye_radius,  # ;
        left_eye_y + eye_radius,  # ;
        fill="white",  # ;
        outline="",  # ;
    )  # ;

    # 8. Create a white oval for the right eye using the canvas.create_oval method on the canvas object. Pass in the right_eye_x - eye_radius, right_eye_y - eye_radius, right_eye_x + eye_radius, right_eye_y + eye_radius as the first 4 arguments. Set fill to "white" and outline to an empty string.
    canvas.create_oval(  # ;
        right_eye_x - eye_radius,  # ;
        right_eye_y - eye_radius,  # ;
        right_eye_x + eye_radius,  # ;
        right_eye_y + eye_radius,  # ;
        fill="white",  # ;
        outline="",  # ;
    )  # ;

    # 9. Create a variable called pupil_radius and set it to 50.
    pupil_radius = 50  # ;

    if is_mouse_inside_eye(
        left_eye_x, left_eye_y, eye_radius, pupil_radius, event.x, event.y
    ):
        # 10. Create a black oval for the pupil using the canvas.create_oval method on the canvas object. Pass in event.x - pupil_radius, event.y - pupil_radius, event.x + pupil_radius, event.y + pupil_radius as the first 4 arguments. Set fill to "black" and outline to an empty string.
        canvas.create_oval(  # ;
            event.x - pupil_radius,  # ;
            event.y - pupil_radius,  # ;
            event.x + pupil_radius,  # ;
            event.y + pupil_radius,  # ;
            fill="black",  # ;
            outline="",  # ;
        )  # ;
    else:
        position = get_eye_position(
            left_eye_x, left_eye_y, eye_radius, pupil_radius, event.x, event.y
        )
        # 11. Create a black oval for the pupil using the canvas.create_oval method on the canvas object. Pass in position.x - pupil_radius, position.y - pupil_radius, position.x + pupil_radius, position.y + pupil_radius as the first 4 arguments. Set fill to "black" and outline to an empty string.
        canvas.create_oval(
            position.x - pupil_radius,
            position.y - pupil_radius,
            position.x + pupil_radius,
            position.y + pupil_radius,
            fill="black",
            outline="",
        )

    if is_mouse_inside_eye(
        right_eye_x, right_eye_y, eye_radius, pupil_radius, event.x, event.y
    ):
        # 12. Create a black oval for the pupil using the canvas.create_oval method on the canvas object. Pass in event.x - pupil_radius, event.y - pupil_radius, event.x + pupil_radius, event.y + pupil_radius as the first 4 arguments. Set fill to "black" and outline to an empty string.
        canvas.create_oval(  # ;
            event.x - pupil_radius,  # ;
            event.y - pupil_radius,  # ;
            event.x + pupil_radius,  # ;
            event.y + pupil_radius,  # ;
            fill="black",  # ;
            outline="",  # ;
        )  # ;
    else:
        position = get_eye_position(
            right_eye_x, right_eye_y, eye_radius, pupil_radius, event.x, event.y
        )
        # 13. Create a black oval for the pupil using the canvas.create_oval method on the canvas object. Pass in position.x - pupil_radius, position.y - pupil_radius, position.x + pupil_radius, position.y + pupil_radius as the first 4 arguments. Set fill to "black" and outline to an empty string.
        canvas.create_oval(  # ;
            position.x - pupil_radius,  # ;
            position.y - pupil_radius,  # ;
            position.x + pupil_radius,  # ;
            position.y + pupil_radius,  # ;
            fill="black",  # ;
            outline="",  # ;
        )  # ;


# The below code is used to determine if the mouse is inside the eye. Do not modify it.
def is_mouse_inside_eye(
    eye_center_x, eye_center_y, eye_radius, pupil_radius, mouse_x, mouse_y
):
    dist_x = mouse_x - eye_center_x
    dist_y = mouse_y - eye_center_y
    distance = math.sqrt((dist_x * dist_x) + (dist_y * dist_y))
    if distance < eye_radius - pupil_radius:
        return True
    return False


# The below code is used to calculate the position of the pupil. Do not modify it.
def get_eye_position(
    eye_center_x, eye_center_y, eye_radius, pupil_radius, mouse_x, mouse_y
):
    class Position:
        x = float()
        y = float()

    position = Position()
    angle = math.atan2(mouse_y - eye_center_y, mouse_x - eye_center_x)
    position.x = eye_center_x + ((eye_radius - pupil_radius) * math.cos(angle))
    position.y = eye_center_y + ((eye_radius - pupil_radius) * math.sin(angle))
    return position


# The below code is used to create the window and canvas. Do not modify it.
root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

setup()
root.bind("<Motion>", draw)
root.mainloop()
