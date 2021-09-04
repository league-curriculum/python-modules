"""
 Create an app that checks the user's typing skills
"""
import tkinter as tk
from PigLatinConverter import PigLatinConverter

class PigLatinTranslator(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize an Entry (tk.Entry) for the input text

        # TODO: Declare and initialize a Button (tk.Button) that will translate
        #  the input text to pig latin when pressed

        # TODO: Declare and initialize an label (tk.Label) for the translated
        #  text

        # TODO: Look at the example image () and place all the
        #  components in the same order

        # TODO: Call the label's bind() method to call the on_key_release()
        #  method when a key is released


    def on_key_press(self, event):
        print('button pressed!')

        # TODO: Use the _c_PigLatinTranslator.translate() method to translate
        #  the text in the input entry and set the text in the output entry


if __name__ == '__main__':
    pass
    # TODO: Create a new _c_PigLatinTranslator object and set the title and geometry.
    #  Remember to call mainloop() at the end
