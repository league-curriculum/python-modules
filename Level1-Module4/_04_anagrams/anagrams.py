"""
Build an anagram game!
http://anagramica.com/api/
"""
import random, json
import tkinter as tk
from tkinter import messagebox

# TODO Use this dictionary of anagrams to create an anagrams GUI word game
word_anagrams = {
    "action": ["cation"],
    "agree": ["eager"],
    "calm": ["clam"],
    "charming": ["marching"],
    "clean": ["lance"],
    "cool": ["loco"],
    "creative": ["reactive"],
    "delight": ["lighted"],
    "earnest": ["eastern", "nearest"],
    "easy": ["ayes", "yeas"],
    "free": ["reef"],
    "great": ["grate"],
    "green": ["genre"],
    "grin": ["ring"],
    "hearty": ["earthy"],
    "idea": ["aide"],
    "ideal": ["ailed"],
    "keen": ["knee"],
    "lively": ["evilly", "vilely"],
    "lovely": ["volley"],
    "merit": ["miter", "remit", "timer"],
    "open": ["nope", "peon", "pone"],
    "perfect": ["prefect"],
    "prepared": ["dapperer"],
    "quiet": ["quite"],
    "refined": ["definer"],
    "restored": ["resorted", "rostered"],
    "reward": ["drawer", "redraw", "warder", "warred"],
    "rewarding": ["redrawing", "wardering"],
    "right": ["girth"],
    "secure": ["rescue"],
    "simple": ["impels"],
    "smile": ["limes", "miles", "slime"],
    "super": ["puers", "purse"],
    "tops": ["opts", "post", "pots", "spot", "stop"],
    "unreal": ["neural"],
    "wonderful": ["underflow"],
    "zeal": ["laze"]}

class Anagram(tk.Tk):

    def __init__(self):
        super().__init__()

        self.guesses = 5
        self.random_word, self.anagrams = self.get_new_word()
        self.num_anagrams_to_guess = len(self.anagrams)

        label_str = 'Guess the ' + str(self.num_anagrams_to_guess)
        if len(self.anagrams) < 2:
            label_str += ' anagram for the word: '
        else:
            label_str += ' anagrams for the word: '
        self.label = tk.Label(self, text=label_str)
        self.label.place(relx=0, rely=0, relwidth=0.5, relheight=0.33)

        self.word_label = tk.Label(self, text=self.random_word)
        self.word_label.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.33)

        self.restart_button = tk.Button(self, bg='light gray', text='Get New Word!')
        self.restart_button.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.33)

        self.guess_remaining_label = tk.Label(self, text='Guesses remaining: ' + str(self.guesses))
        self.guess_remaining_label.place(relx=0, rely=0.33, relwidth=0.5, relheight=0.33)

        self.entry_guess = tk.Entry(self)
        self.entry_guess.place(relx=0.5, rely=0.33, relwidth=0.5, relheight=0.33)

        self.correct_guesses_label = tk.Label(self)
        self.correct_guesses_label.place(relx=0, rely=0.66, relwidth=1, relheight=0.33)

        self.entry_guess.bind('<KeyPress>', self.on_guess)
        self.restart_button.bind('<ButtonPress>', self.restart)

    def restart(self, event=None):
        if len(self.anagrams) > 0:
            messagebox.showinfo('Answers', 'The anagrams were: ' + repr(self.anagrams))

        self.random_word, self.anagrams = self.get_new_word()
        self.guesses = 5
        self.guess_remaining_label.configure(text='Guesses remaining: ' + str(self.guesses))
        self.word_label.configure(text=self.random_word)
        self.entry_guess.configure(text='')

        label_str = 'Guess the ' + str(self.num_anagrams_to_guess)
        if len(self.anagrams) < 2:
            label_str += ' anagram for the word: '
        else:
            label_str += ' anagrams for the word: '
        self.label.configure(text=label_str)

    def get_new_word(self):
        list_of_keys = list(word_anagrams.keys())
        random_word = random.choice(list_of_keys)
        anagrams = word_anagrams[random_word]

        return random_word, anagrams

    def on_guess(self, event):
        key = str(event.keysym)

        if key.lower() == 'return' and len(self.anagrams) > 0:
            word_guessed = self.entry_guess.get()

            if word_guessed != self.random_word and word_guessed in self.anagrams:
                anagrams_guessed = self.correct_guesses_label['text'] + word_guessed + '\n'
                self.correct_guesses_label.configure(text=anagrams_guessed)
                self.anagrams.remove(word_guessed)

                if len(self.anagrams) == 0:
                    messagebox.showinfo('WINNER', 'You found all the anagrams!')
                    self.restart()
                else:
                    label_str = 'Guess the ' + str(self.num_anagrams_to_guess)
                    if len(self.anagrams) < 2:
                        label_str += ' anagram for the word: '
                    else:
                        label_str += ' anagrams for the word: '
                    self.label = tk.Label(self, text=label_str)

            else:
                self.guesses -= 1
                self.guess_remaining_label.configure(text='Guesses remaining: ' + str(self.guesses))
                messagebox.showerror('', 'INCORRECT!')

                if self.guesses == 0:
                    print(self.anagram.values())


if __name__ == '__main__':
    game = Anagram()
    game.title('League Anagram Game')
    game.geometry('400x100')
    game.mainloop()
