"""
Card class
"""
import random
import time
import tkinter as tk

class MemoryMatch(tk.Tk):
    WIDTH = 1090
    HEIGHT = 500
    TOTAL_BUTTONS = 52

    def __init__(self):
        super().__init__()

        # 4 copies of each value
        num_copies_each_value = 4
        buttons_per_row = MemoryMatch.TOTAL_BUTTONS / 4
        button_width, button_height = self.setup_buttons(buttons_per_row)

        self.button_value_dict = dict()

        self.values = list()
        for i in range(MemoryMatch.TOTAL_BUTTONS):
            value = int(i % (MemoryMatch.TOTAL_BUTTONS / num_copies_each_value))
            self.values.append(value)

        random.shuffle(self.values)

        self.first_button_pressed = None

        for i in range(MemoryMatch.TOTAL_BUTTONS):
            row_num = int(i / buttons_per_row)
            col_num = int(i % buttons_per_row)
            row_y = row_num * button_height
            col_x = col_num * button_width

            button = tk.Button(self, text='', fg='black', font=('arial', 24, 'bold'))
            button.place(x=col_x, y=row_y, width=button_width, height=button_height)

            # TODO: Call the button's bind() method to call the on_button_press()
            #  method when a mouse button is pressed
            #  example: self.joke_button.bind('<ButtonPress>', self.on_button_press)
            button.bind('<ButtonPress>', self.on_button_press)

            # TODO: Add the button to the list of buttons
            self.button_value_dict[button] = self.values[i]

    def on_button_press(self, event):
        if event.widget['state'] != tk.DISABLED:
            button_value = self.button_value_dict[event.widget]
            event.widget.configure(text=str(button_value), state=tk.DISABLED)

            self.update_idletasks()
            time.sleep(0.35)

            if self.first_button_pressed is None:
                self.first_button_pressed = event.widget
            else:
                value_1 = self.button_value_dict[event.widget]
                value_2 = self.button_value_dict[self.first_button_pressed]

                if value_1 == value_2:
                    event.widget.configure(bg='light green', state=tk.DISABLED)
                    self.first_button_pressed.configure(bg='light green', state=tk.DISABLED)
                else:
                    event.widget.configure(text='')
                    self.first_button_pressed.configure(text='')

                    # No match, reset buttons
                    event.widget.configure(state=tk.NORMAL)
                    self.first_button_pressed.configure(state=tk.NORMAL)

                # Second button pressed, automatically reset
                # At the bottom where first button info is no longer needed
                self.first_button_pressed = None

    def setup_buttons(self, buttons_per_row):
        # Window size needs to be updated immediately here so the
        # window width/height variables can be used below
        self.geometry('%sx%s' % (MemoryMatch.WIDTH, MemoryMatch.HEIGHT))
        self.update_idletasks()

        num_rows = int(MemoryMatch.TOTAL_BUTTONS / buttons_per_row)
        if MemoryMatch.TOTAL_BUTTONS % buttons_per_row != 0:
            num_rows += 1

        button_width = int(self.winfo_width() / buttons_per_row)
        button_height = int(self.winfo_height() / num_rows)

        return button_width, button_height

if __name__ == '__main__':
    game = MemoryMatch()
    game.title('League Python Memory Game')
    game.mainloop()
