import random
import tkinter as tk


class Hangman(tk.Tk):
    dict_word_list = None

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.entered_text = tk.StringVar()
        self.label = None
        self.restart_button = None
        self.random_word = None

        # 5. Make a new instance variable to hold the word being guessed

        self.initialize()

    def initialize(self):
        # Get Random word from dictionary
        Hangman.read_words_file()
        self.random_word = Hangman.get_random_word()
        print(self.random_word)

        # Setup label to display keys pressed by the user
        self.label = tk.Label(self, bg='light grey', textvariable=self.entered_text)
        self.label.place(relwidth=1, relheight=1)

        self.setup_new_word()

    def setup_new_word(self):
        # 6. Create an string of underscores that's the same length of the random word

        # 7. Set the string of underscores using entered_text.set()

        # 8. Delete 'pass'
        pass

    def key_pressed(self, event):
        key = str(event.char)
        print("pressed " + key)

        # 9. Check if the key that was pressed is within the guess string
        # You can change a string into a list by doing: my_list = list(my_string)
        # You can change a list into a string by doing: my_string = ''.join(my_list)

        # 10. If the guess string matches the random word,
        # Print a message/pop-up telling the user they won!

    # --------------------------- DO NOT EDIT this method ---------------------
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

    # --------------------------- DO NOT edit this method ---------------------
    @staticmethod
    def get_random_word():
        if Hangman.dict_word_list is None or len(Hangman.dict_word_list) == 0:
            print("ERROR: Dictionary text file not loaded")
            return

        random_word = random.choice(Hangman.dict_word_list)

        return random_word


if __name__ == '__main__':
    # 1. Delete 'pass' and make a new Hangman game, example
    # game = Hangman(None)
    pass

    # 2. Set your game title

    # 3. Add a key listener to your game
    # game.bind("<Key>", game.key_pressed)

    # 4. Run your game's mainloop()
