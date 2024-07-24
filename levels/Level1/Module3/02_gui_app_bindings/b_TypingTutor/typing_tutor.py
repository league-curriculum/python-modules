"""
 Create an app that checks the user's typing skills
"""
import tkinter as tk
import random

# Use this function to return a random character
def generate_random_letter():
    return chr(random.randint(0, 25) + ord('a'))


class TypingTutor(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize a member variable to hold a
        #  random letter to type
        self.random_letter = generate_random_letter()

        # TODO: Declare and initialize a label (tk.Label) and
        self.letter_label = tk.Label(self, text=self.random_letter, bg='grey', fg='black',
                                     font=('arial', 64, 'bold'), relief='solid')

        # TODO: Place the label in the center of the window
        self.letter_label.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        # TODO: Call the label's focus_set() method so key presses can be detected
        self.letter_label.focus_set()

        # TODO: Call the label's bind() method to call the on_key_release()
        #  method when a key is released
        #  example: self.label.bind('<KeyRelease>', self.on_key_release)
        self.letter_label.bind('<KeyRelease>', self.on_key_release)

    def on_key_release(self, event):
        letter_pressed = event.char
        print('key ' + letter_pressed + ' released!')

        # TODO: If the user pressed the correct key,
        #         change the label's background to green
        #       If the user pressed the wrong key,
        #         change the label's background to red
        #  example: self.label.configure(bg='green')
        if letter_pressed == self.random_letter:
            self.letter_label.configure(bg='green')
        else:
            self.letter_label.configure(bg='red')

        # TODO: Get a new random letter and place it on the label
        #  example: self.label.configure(text=self.rand_letter)
        self.random_letter = generate_random_letter()
        self.letter_label.configure(text=self.random_letter)




# TODO: Create a new _b_TypingTutor object and set the title and geometry.
#  Remember to call mainloop() at the end
game = TypingTutor()
game.title('Typing Tutor')
game.geometry('600x400')
game.mainloop()
