"""
 Create a whack-a-mole game using Tkinter buttons!
"""
import random
import tkinter as tk


class Whack(tk.Tk):

    def __init__(self, num_buttons):
        super().__init__()

        # Window size needs to be updated immediately here so the
        # window width/height variables can be used below
        self.geometry('800x600')
        self.update_idletasks()

        columns_per_row = 5
        num_rows = int(num_buttons / columns_per_row)
        if num_buttons % columns_per_row != 0:
            num_rows += 1

        button_width = int(self.winfo_width() / columns_per_row)
        button_height = int(self.winfo_height() / num_rows)

        # TODO: Create a member variable for the list of buttons
        self.buttons = list()

        # TODO: Create a member variable for the random mole button and
        #  initialize it to None
        self.mole_button = None

        # TODO: Use a loop to create enough buttons to fill the window.
        #  Use the 'columns_per_row', 'button_width', 'button_height' variables
        #  when calling button.place() to put each button in the correct
        #  position
        for i in range(num_buttons):
            row_num = int(i / columns_per_row)
            col_num = int(i % columns_per_row)
            row_y = row_num * button_height
            col_x = col_num * button_width

            button = tk.Button(self, fg='blue', font=('arial', 24, 'bold'))
            button.place(x=col_x, y=row_y, width=button_width, height=button_height)

            # TODO: Call the button's bind() method to call the on_button_press()
            #  method when a mouse button is pressed
            #  example: self.joke_button.bind('<ButtonPress>', self.on_button_press)
            button.bind('<ButtonPress>', self.on_button_press)

            # TODO: Add the button to the list of buttons
            self.buttons.append(button)

        # TODO: Set the mole button to the output of the random.choice() method
        #  to return a random button from the list of buttons
        self.mole_button = random.choice(self.buttons)

        # TODO: Call the mole button's config(text='mole!') method to set its
        #  text to 'mole!'
        self.mole_button.config(text='mole!')

    def on_button_press(self, event):
        button_pressed = event.widget
        print('button ' + repr(button_pressed) + ' clicked!')

        # Stop if button pressed is not the mole button!
        if button_pressed != self.mole_button:
            return

        # Clear text for current mole button
        self.mole_button.configure(text='')

        # Get new random mole button that's different from the current one
        button = random.choice(self.buttons)
        while button is self.mole_button:
            button = random.choice(self.buttons)
        self.mole_button = button

        # Change the text for the new mole button
        self.mole_button.configure(text='mole!')


if __name__ == '__main__':
    # Must be 5 or greater
    num_of_buttons = 25

    game = Whack(num_of_buttons)
    game.title('Whack-a-Mole')
    game.mainloop()
