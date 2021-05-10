import random
import tkinter as tk
from tkinter import messagebox

# TODO 1) Complete the function to return a string with as many
#  underscores (_) as there are letters in the word to guess
#  word_to_guess = orange (a string)
#  return          ______ (a string with 6 underscores)
def setup_new_word(word_to_guess):

    return str()

# TODO 2) Complete the function to return whether the letter is in
#  the word to guess
#  word_to_guess = orange (a string)
#  letter = o (a string)
#  return True
def check_letter_in_word(word_to_guess, letter):

    return False

# TODO 3) Complete the function to return the current guess with the
#  letter in the same places (index) of the word to guess. For example,
#       word to guess = orange (a string)
#       current guess = o__n_e (a string)
#       letter = g
#       return o__nge (a string)
#  Remember that strings can't be changed directly!
def replace_letter_in_word(word_to_guess, current_guess, letter):

    return str()

# ====================== DO NOT EDIT THE CODE BELOW ===========================

class Hangman(tk.Tk):
    dict_word_list = None

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.entered_text = tk.StringVar()
        self.lives_text = tk.StringVar()
        self.lives = 10
        self.label = None
        self.lives_label = None
        self.restart_button = None
        self.hint_button = None
        self.random_word = None
        self.wtg = ''

        self.initialize()

    def initialize(self):
        # Get Random word from dictionary
        Hangman.read_words_file()
        self.get_new_random_word()

        # UNCOMMENT TO SHOW HIDDEN WORD
        #print(self.random_word)

        # Setup label to display keys pressed by the user
        self.label = tk.Label(self, bg='light grey', textvariable=self.entered_text)
        self.label.place(relx=0, rely=0, relwidth=1, relheight=0.5)

        self.lives_label = tk.Label(self, bg='light grey', textvariable=self.lives_text)
        self.lives_label.place(relx=0, rely=0.5, relwidth=1, relheight=0.25)

        self.restart_button = tk.Button(self, bg='light grey', text='restart', command=self.get_new_random_word)
        self.restart_button.place(relx=0.15, rely=0.8, relwidth=0.25, relheight=0.15)

        self.hint_button = tk.Button(self, bg='light grey', text='hint', command=self.give_hint)
        self.hint_button.place(relx=0.5, rely=0.8, relwidth=0.25, relheight=0.15)

    def give_hint(self):
        if self.lives > 4 and self.random_word != self.wtg:
            unguessed_letter = None

            while True:
                random_index = random.randint(0, len(self.wtg)-1)
                if self.wtg[random_index] == '_':
                    unguessed_letter = self.random_word[random_index]
                    break

            self.wtg = replace_letter_in_word(self.random_word, self.wtg, unguessed_letter)
            self.entered_text.set(self.wtg)
            self.lives -= 4
            self.lives_text.set('guesses: ' + str(self.lives))
            self.check_words_match()
        else:
            messagebox.showerror(None, 'You need at least 4 lives. You have ' + str(self.lives))

    def get_new_random_word(self):
        if self.random_word is not None and self.lives > 0 and self.wtg != self.random_word:
            messagebox.showinfo(None, 'The word was: ' + self.random_word)

        self.random_word = Hangman.get_random_word()
        self.setup_new_word()

    def setup_new_word(self):
        self.wtg = setup_new_word(self.random_word)
        self.entered_text.set(self.wtg)
        self.lives = 10
        self.lives_text.set('guesses: ' + str(self.lives))

    def check_words_match(self):
        if self.wtg == self.random_word:
            messagebox.showinfo("WINNER", "Congratulations, you win!")
            self.get_new_random_word()

    def key_pressed(self, event):
        key = str(event.char)
        print("pressed " + key)

        if self.lives > 0:
            if check_letter_in_word(self.random_word, key):
                self.wtg = replace_letter_in_word(self.random_word, self.wtg, key)
                self.entered_text.set(self.wtg)
                self.check_words_match()
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
    game.configure(bg='light grey')
    game.bind("<Key>", game.key_pressed)
    game.mainloop()
