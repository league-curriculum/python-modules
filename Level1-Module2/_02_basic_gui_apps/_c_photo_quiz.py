"""
Photo Quiz: Ask a question about a photo and guess the answer!
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL import Image, ImageTk

def create_image(filename, width, height):
    image_obj = None

    try:
        image = Image.open(filename)
        image = image.resize((width, height), Image.ANTIALIAS)
        image_obj = ImageTk.PhotoImage(image=image)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj

# ======================= DO NOT EDIT THE CODE ABOVE =========================

# TODO 0) Find at least 3 interesting photos (2 are provided if you want
#  to use those)

# TODO 1) Create a new tkinter class
class PhotoQuiz(tk.Tk):

    # TODO 2) Create a constructor
    def __init__(self):

        # TODO 3) call Tk's constructor,
        #  super().__init__()
        super().__init__()

        # TODO 4) Create a label and place it
        self.photo_label = tk.Label(self)
        self.photo_label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


if __name__ == '__main__':
    # TODO 5) Create an object of the tkinter class
    app = PhotoQuiz()

    # TODO 6) Set the app window width and height using geometry()
    app.title('Photo Quiz')
    app.geometry('500x500')

    # TODO 7) Declare and initialize a score variable
    score = 0

    # TODO 8) Create an image object using the create_image function above
    #  and store it in a variable
    image_object = create_image('fossil.jpg', 400, 400)

    # TODO 9) Set the image onto the class's label using the configure method,
    #  for example:
    #  app.photo_label.configure(image=image_object)
    app.photo_label.configure(image=image_object)

    # TODO 10) Use a pop-up (simpledialog) to ask the user a question
    #  relating to the image and tell them if they get the right answer.
    answer = simpledialog.askstring(None, "These bones belong to what kind of animal?")

    # TODO 11) If the answer is correct, increase the score by 1
    if 'dinosaur' in answer.lower():
        score += 1

    # TODO 12) Repeat the steps to show a different photo and ask a different
    #  question
    image_object = create_image('carrots.jpg', 400, 400)
    app.photo_label.configure(image=image_object)
    answer = simpledialog.askstring(None, "What vegetable is this?")
    if 'carrot' in answer.lower():
        score += 1

    # TODO 13) Display the score to the user after asking the last question
    messagebox.showinfo(None, 'Your score is: ' + str(score))
