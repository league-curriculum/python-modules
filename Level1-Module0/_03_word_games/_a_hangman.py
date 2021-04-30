import random
import tkinter as tk
from tkinter import messagebox

# TODO 1) Complete the function to return a string with as many
#  underscores (_) as there are letters in the word to guess
def setup_new_word(word_to_guess):
    word = str()

    for i in range(len(word_to_guess)):
        word += '_'

    return word

# TODO 2) Complete the function to return whether the letter is in
#  the word to guess
def check_letter_in_word(word_to_guess, letter):
    if letter in word_to_guess:
        return True
    return False

# TODO 3) Complete the function to return the current guess with the
#  letter in the same places (index) of the word to guess. For example,
#       word to guess = orange
#       current guess = o__n_e
#       letter = g
#       return o__nge
def replace_letter_in_word(word_to_guess, current_guess, letter):
    for i in range(len(word_to_guess)):
        if word_to_guess[i] == letter:
            current_guess[i] = letter

    return current_guess

class Hangman(tk.Tk):
    dict_word_list = None

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.entered_text = tk.StringVar()
        self.lives_text = tk.StringVar()
        self.lives = 10
        self.label = None
        self.restart_button = None
        self.random_word = None
        self.wtg = ''

        self.initialize()

    def initialize(self):
        # Get Random word from dictionary
        Hangman.read_words_file()
        self.random_word = Hangman.get_random_word()

        # UNCOMMENT TO SHOW HIDDEN WORD
        #print(self.random_word)

        # Setup label to display keys pressed by the user
        self.label = tk.Label(self, bg='light grey', textvariable=self.entered_text)
        self.label.place(relx=0, rely=0, relwidth=1, relheight=0.5)

        self.label = tk.Label(self, bg='light grey', textvariable=self.lives_text)
        self.label.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

        self.setup_new_word()

    def setup_new_word(self):
        self.wtg = setup_new_word(self.random_word)
        self.entered_text.set(self.wtg)
        self.lives_text.set('guesses: ' + str(self.lives))

    def key_pressed(self, event):
        key = str(event.char)
        print("pressed " + key)

        # 8. Check if the key that was pressed is within the guess string
        # You can change a string into a list by doing: my_list = list(my_string)
        # You can change a list into a string by doing: my_string = ''.join(my_list)
        if check_letter_in_word(self.random_word, key):
            self.wtg = list(self.wtg)
            self.wtg = replace_letter_in_word(self.random_word, self.wtg, key)
            self.wtg = ''.join(self.wtg )
            self.entered_text.set(self.wtg)

            if self.wtg == self.random_word:
                messagebox.showinfo("WINNER", "Congratulations, you win!")
        else:
            self.lives -= 1
            self.lives_text.set('guesses: ' + str(self.lives))
            if self.lives == 0:
                messagebox.showinfo("Lose", "You lose! The correct word was " + self.random_word)

    @staticmethod
    def read_words_file():
        # Only need to be read once
        if Hangman.dict_word_list is None:
            file_handle = None
            word_file = "dictionary.txt"

            # 'with' statement will automatically close the file afterwards
            with open(word_file) as file_handle:
                # Populate list with all words read from file
                Hangman.dict_word_list = file_handle.read().splitlines()

                # Sort the list so it'll be easier to find plurals
                Hangman.dict_word_list.sort()

    @staticmethod
    def get_random_word():
        if Hangman.dict_word_list is None or len(Hangman.dict_word_list) == 0:
            print("ERROR: Dictionary text file not loaded")
            return

        random_word = random.choice(Hangman.dict_word_list)

        return random_word


if __name__ == '__main__':
    game = Hangman(None)
    game.title("Hangman")
    game.bind("<Key>", game.key_pressed)
    game.mainloop()
