"""
 Create a whack-a-mole game using Tkinter buttons!
"""
import random
import tkinter as tk


class Whack(tk.Tk):

    def __init__(self, num_buttons):
        super().__init__()

        columns_per_row = 5
        button_width, button_height = self.setup_buttons(num_buttons, columns_per_row)

        # TODO: Create a member variable for the list of buttons

        # TODO: Create a member variable for the random mole button and
        #  initialize it to None

        # TODO: Use a loop to create enough buttons to fill the window.
        #  Use the 'columns_per_row', 'button_width', 'button_height' variables
        #  when calling button.place() to put each button in the correct
        #  position
        for i in range(num_buttons):
            row_num = int(i / columns_per_row)
            col_num = int(i % columns_per_row)
            row_y = row_num * button_height
            col_x = col_num * button_width

            # TODO: Call the button's bind() method to call the on_button_press()
            #  method when a mouse button is pressed
            #  example: self.joke_button.bind('<ButtonPress>', self.on_button_press)

            # TODO: Add the button to the list of buttons


        # TODO: Set the mole button to the output of the random.choice() method
        #  to return a random button from the list of buttons

        # TODO: Call the mole button's config(text='mole!') method to set its
        #  text to 'mole!'

    def on_button_press(self, event):
        button_pressed = event.widget
        print('button ' + repr(button_pressed) + ' clicked!')

        # TODO: return if button pressed is not the mole button!

        # TODO: Clear text for current mole button using
        #  the buttons' configure() method

        # TODO: Get new random mole button that's different from the current one

        # TODO: Change the text for the new mole button using
        #  the buttons' configure() method


    def setup_buttons(self, num_buttons, columns_per_row):
        # Window size needs to be updated immediately here so the
        # window width/height variables can be used below
        self.geometry('800x600')
        self.update_idletasks()

        num_rows = int(num_buttons / columns_per_row)
        if num_buttons % columns_per_row != 0:
            num_rows += 1

        button_width = int(self.winfo_width() / columns_per_row)
        button_height = int(self.winfo_height() / num_rows)

        return button_width, button_height


if __name__ == '__main__':
    # Must be 5 or greater
    num_of_buttons = 25

    game = Whack(num_of_buttons)
    game.title('Whack-a-Mole')
    game.mainloop()
