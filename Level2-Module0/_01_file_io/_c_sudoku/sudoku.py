"""
 Create a Sudoku game!
"""
import random
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

# TODO 1) Look at the sudo_grids.txt file. There are multiple starting sudoku
#  grids inside. Complete the function below with the following requirements:
#  1. Open the sudoku_grids_file file for reading
#  2. Select a random sudoku grid
#  3. Read the random grid picked that was picked and return each row as an
#     element in a list of strings (not integers), for example:
#     ['003020600',
#      '900305001',
#      '001806400',
#      '008102900',
#      '700000008',
#      '006708200',
#      '002609500',
#      '800203009',
#      '005010300]
def open_sudoku_file(sudoku_grids_file):
    return None

# TODO 2) Complete the function below with the following requirements:
#  1. Give the save_file input variable a default string
#  2. Open the save_file input variable for writing.
#     If the file already exists, overwrite it.
#  3. Write the contents of the sudoku_grid_list to the file, where each
#     element in the list is a new line in the file. The file should look
#     similar to this:
#       003020600
#       900305001
#       001806400
#       008102900
#       700000008
#       006708200
#       002609500
#       800203009
#       005010300
#  *NOTE: DON'T forget the new line ('\n') at the end!
def on_save_button(sudoku_grid_list, save_file='saved.txt'):
    return None

# TODO 3) Complete the function below with the following requirements:
#  1. Give the saved_file input variable a default string
#  2. Open the saved_file input variable for reading.
#  3. Return a list of strings containing the integers (as strings!) for
#     each row, similar to TODO 1) open_sudoku_file()
#  4. If the file could not be found, return None and an error message
def on_load_button(saved_file='saved.txt'):
    return None

class Sudoku(tk.Tk):
    sudoku_grids_file = 'sudoku_grids.txt'

    def __init__(self):
        super().__init__()

        # Window size needs to be updated immediately here so the
        # window width/height variables can be used below
        self.geometry('800x600')
        self.update_idletasks()

        self.sudoku_grid = None

        #
        # Setup cells to hold the numbers
        #
        self.entries = list()
        self.entries_rows = [list(), list(), list(), list(), list(), list(), list(), list(), list()]
        self.entries_cols = [list(), list(), list(), list(), list(), list(), list(), list(), list()]

        self.entries_per_row = 9
        self.entries_per_col = 9
        num_frames = 9
        cols_per_frame = 3
        rows_per_frame = cols_per_frame
        entries_per_frame = cols_per_frame * rows_per_frame

        # +1 to leave room on the right for the load and solve buttons
        entry_width = float(self.winfo_width() / (self.entries_per_col + 1))
        entry_height = float(self.winfo_height() / self.entries_per_row)

        #
        # Setup and build 3x3 cell frames
        #
        frame_width = cols_per_frame * entry_width
        frame_height = rows_per_frame * entry_height
        self.frames = list()

        for i in range(num_frames):
            frame_x = (i % cols_per_frame) * frame_width
            frame_y = int(i / rows_per_frame) * frame_height
            frame = tk.Frame(self, highlightbackground="black", highlightthickness=1)
            frame.place(x=frame_x, y=frame_y, width=frame_width, height=frame_height)
            self.frames.append(frame)

            #
            # Build cells inside 3x3 frames
            #
            for k in range(entries_per_frame):
                row_num = int(k / cols_per_frame)
                col_num = int(k % rows_per_frame)
                row_y = row_num * entry_height
                col_x = col_num * entry_width

                # %d = action (insert=1, delete=0), %P = key value, %s = current value
                # https://tcl.tk/man/tcl8.6/TkCmd/entry.htm#M16
                validate_cmd = (self.register(self.num_check), '%d', '%P', '%s')

                entry = tk.Entry(frame, justify='center', validate='key', vcmd=validate_cmd,
                                 fg='blue', font=('arial', 24, 'bold'))
                entry.place(x=col_x, y=row_y, width=entry_width, height=entry_height)

                self.entries.append(entry)

                row_index = (3 * int(i / 3)) + int(k / 3)
                col_index = (3 * int(i % 3)) + int(k % 3)
                self.entries_rows[row_index].append(entry)
                self.entries_cols[col_index].append(entry)

        #
        # Setup and build menu buttons
        #
        self.new_game_button = tk.Button(self, text='New Game')
        self.check_answer_button = tk.Button(self, text='Check Answer')
        self.save_button = tk.Button(self, text='Save')
        self.load_button = tk.Button(self, text='Load')

        self.new_game_button.bind('<ButtonPress>', self.on_new_game_button)
        self.check_answer_button.bind('<ButtonPress>', self.on_check_answer_button)
        self.save_button.bind('<ButtonPress>', lambda event: self.on_save_button())
        self.load_button.bind('<ButtonPress>', lambda event: self.on_load_button())

        menu_x = 3 * frame_width
        menu_width = self.winfo_width() - menu_x
        menu_button_height = 50
        self.new_game_button.place(x=menu_x, y=0, w=menu_width, h=menu_button_height)
        self.check_answer_button.place(x=menu_x, y=menu_button_height, w=menu_width,
                                       h=menu_button_height)
        self.save_button.place(x=menu_x, y=2*menu_button_height, w=menu_width, h=menu_button_height)
        self.load_button.place(x=menu_x, y=3*menu_button_height, w=menu_width, h=menu_button_height)

    def on_save_button(self):
        on_save_button(self.entries_to_list())

    def on_load_button(self):
        string_list = on_load_button()

        # Remove new lines at the end
        string_list = [row[0 : len(row)-1] for row in string_list]

        if len(string_list) != 9:
            messagebox.showerror('ERROR', 'ERROR: ' + str(len(string_list)) +
                                 'rows in loaded file, expected 9')

        for row, row_string in enumerate(string_list):
            for offset, value in enumerate(row_string):
                entry = self.entries_rows[row][offset]

                entry.configure(state='normal', bg='white')
                entry.delete(0, 'end')

                if value == '0':
                    entry.insert(0, '')
                else:
                    entry.insert(0, value)

        self.update_idletasks()

    def entries_to_list(self):
        string_list = list()

        for entries_row in self.entries_rows:
            row_str = str()

            for entry in entries_row:
                if entry.get() == '':
                    row_str += '0'
                else:
                    row_str += entry.get()

            string_list.append(row_str)

        return string_list

    def num_check(self, action, value_if_allowed, prior_value):
        # Allow deleting characters
        if action == '0':
            return True

        # Don't allow more than 1 number in the text field
        if prior_value == '':
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    def on_new_game_button(self, event):
        print('new game button pressed')

        #
        # Clear all the sudoku cells
        #
        for entry in self.entries:
            entry.configure(state='normal', bg='white')
            entry.delete(0, 'end')

        #
        # Load a starting grid to play
        #
        self.sudoku_grid = open_sudoku_file(Sudoku.sudoku_grids_file)

        #
        # Set the tk.entries with the starting numbers from the read grid
        #
        for row_num, row_entries in enumerate(self.entries_rows):
            row = self.sudoku_grid[row_num]

            for offset in range(self.entries_per_row):
                value = row[offset]

                if value != '0':
                    row_entries[offset].insert(0, str(value))
                    row_entries[offset].configure(state='disabled')

    def on_check_answer_button(self, event):
        print('check answer button pressed')

        # Reset tk.entry colors
        for entry in self.entries:
            entry.configure(state='normal', bg='white')

        #
        # Check all 3x3 frames
        #
        success = self.check_frames()

        #
        # Check all rows
        #
        if success:
            success = self.check_rows()

        #
        # Check all columns
        #
        if success:
            success = self.check_cols()

        if success:
            messagebox.showinfo('Win', "You win!!!")

    def check_cols(self):
        for col_list in self.entries_cols:
            success = self.check_entries(col_list)

            if not success:
                break

        return success

    def check_rows(self):
        for row_list in self.entries_rows:
            success = self.check_entries(row_list)

            if not success:
                break

        return success

    def check_frames(self):
        for frame in self.frames:
            success = self.check_entries(frame.children.values())

            if not success:
                break

        return success

    def check_entries(self, entries):
        success = True
        digits = list()
        entry_sum = 0

        for i, entry in enumerate(entries):
            try:
                value = int(entry.get())

                if value in digits:
                    print('ERROR: Duplicate digit: ' + str(value))
                    success = False
                    break

                digits.append(value)
                entry_sum += int(entry.get())

            except ValueError:
                print('ERROR: No number in cell: ' + str(i))
                success = False
                break

        if success:
            if len(digits) != 9:
                print('ERROR: not all digits 0-9 used, actual number used: ' + str(len(digits)))
                success = False

        if success:
            if entry_sum != 45:
                print('ERROR: entry sum not 45, actual sum: ' + str(entry_sum))
                success = False

        if not success:
            for entry in entries:
                entry.configure(state='normal', bg='red')

        return success


if __name__ == '__main__':
    game = Sudoku()
    game.title('League Sudoku')
    game.mainloop()
