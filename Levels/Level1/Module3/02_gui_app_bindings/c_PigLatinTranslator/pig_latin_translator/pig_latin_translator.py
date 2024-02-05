"""
 Create an app that checks the user's typing skills
"""
import tkinter as tk
from PigLatinConverter import PigLatinConverter

class PigLatinTranslator(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize an Entry (tk.Entry) for the input text
        self.input_entry = tk.Entry(self, font=('arial', 10, 'normal'), relief='solid')

        # TODO: Declare and initialize a Button (tk.Button) that will translate
        #  the input text to pig latin when pressed
        self.translate_button = tk.Button(self, text='Translate', bg='light green', fg='black',
                                          font=('arial', 12, 'normal'), relief='solid')

        # TODO: Declare and initialize an label (tk.Label) for the translated
        #  text
        self.translate_label = tk.Label(self, font=('arial', 10, 'normal'), relief='solid')

        # TODO: Look at the example image () and place all the
        #  components in the same order
        self.input_entry.place(relx=0.01, rely=0.01, relwidth=0.44, relheight=0.90)
        self.translate_button.place(relx=0.45, rely=0.01, relwidth=0.1, relheight=0.90)
        self.translate_label.place(relx=0.55, rely=0.01, relwidth=0.44, relheight=0.90)

        # TODO: Call the label's bind() method to call the on_key_release()
        #  method when a key is released
        self.translate_button.bind('<ButtonPress>', self.on_key_press)

    def on_key_press(self, event):
        print('button pressed!')

        # TODO: Use the _c_PigLatinTranslator.translate() method to translate
        #  the text in the input entry and set the text in the output entry
        translated_text = PigLatinConverter.translate(self.input_entry.get())
        print(translated_text)
        self.translate_label.config(text=translated_text)


# TODO: Create a new _c_PigLatinTranslator object and set the title and geometry.
#  Remember to call mainloop() at the end
game = PigLatinTranslator()
game.title('Pig Latin Translator')
game.geometry('800x50')
game.mainloop()
