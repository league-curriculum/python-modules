import os
import tkinter as tk
from PIL import Image, ImageTk
import simpleaudio as sa

# If simpleaudio is not installed, you can install it by running the following command in the terminal:
# pip install simpleaudio or pip3 install simpleaudio for unix/linux

"""
This is the main code for the WheresWaldo game.

To play the game, follow these steps:
1. Run the script.
2. Click on the image to check if Waldo is found.
3. If Waldo is found, a sound will play and "Found Waldo!" text will be displayed on the canvas.


Note: If you encounter any issues with the sound file, Replace the play_sound method in the check_waldo method with the show_text method to display the "Found Waldo!" text on the canvas.

"""


class WheresWaldo:
    def __init__(self, root):
        """
        Initialize the WheresWaldo game.

        Parameters:
        - root: The root Tkinter window object.
        """
        self.root = root
        self.canvas = tk.Canvas(root, width=1000, height=800)
        self.canvas.pack()
        self.setup_canvas()

    def setup_canvas(self):
        """
        Set up the canvas by loading the Waldo image and binding the click event.
        """
        self.waldo_img = self.load_image("waldo.jpg")
        self.canvas.create_image(0, 0, anchor="nw", image=self.waldo_img)
        self.canvas.bind("<Button-1>", self.check_waldo)

    def load_image(self, filename):
        """
        Load an image from the specified filename.

        Parameters:
        - filename: The name of the image file.

        Returns:
        - The loaded image as a Tkinter PhotoImage object.
        """
        current_directory = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(current_directory, filename)
        image = Image.open(image_path)
        return ImageTk.PhotoImage(image)

    # TODO 1) Create a method called check_waldo that takes an event as the parameter
    # TODO 2) Inside the check_waldo method, check if the x and y coordinates of the event are within the range of the Waldo image. The range of the Waldo image is from (615, 390) to (700, 560). You will use event.x and event.y to check where the mouse is clicked.
    # TODO 3) If the x and y coordinates of the event are within the range of the Waldo image, call the play_sound method with the "woohoo.wav" sound file as the parameter. This will play the sound when Waldo is found. Don't forget to use the self keyword to call the play_sound method.
    def check_waldo(self, event):  # ;
        if 615 <= event.x < 700 and 390 <= event.y < 560:  # ;

            self.play_sound("woohoo.wav")  # ;

    def show_text(self, message):
        """
        Display text on the canvas.

        Parameters:
        - message: The text message to display.
        """
        self.canvas.create_text(500, 400, text=message, font=("Arial", 24))

    def play_sound(self, sound_file):
        """
        Play a sound from the specified sound file.

        Parameters:
        - sound_file: The name of the sound file.

        Returns:
        - The sound object.
        """
        sound_path = os.path.join(os.path.dirname(__file__), sound_file)
        return sa.WaveObject.from_wave_file(sound_path).play()


root = tk.Tk()
app = WheresWaldo(root)
root.mainloop()
