"""
Build an anagram game!
http://anagramica.com/api/
"""
import random
import tkinter as tk
from tkinter import messagebox

import requests
import json

def generate_file():
    word_list = read_words_file()
    anagrams_dict = dict()

    for word in word_list:
        anagram = get_anagram_from_api(word)

        print('Trying ' + word)

        if len(word) < 4 or len(anagram) < 1:
            continue

        if len(anagram['best']) > 1:
            print('--->adding ' + word)
            anagrams = anagram['best']
            anagrams.remove(word)
            anagrams_dict[word] = anagrams

    with open("anagrams.json", "w") as outfile:
        json.dump(anagrams_dict, outfile)


def read_words_file():
    word_list = list()
    file_handle = None
    word_file = "dictionary.txt"

    with open(word_file) as file_handle:
        word_list = file_handle.read().splitlines()

    word_list.sort()

    return word_list

def get_anagram_from_api(letters):
    data = {}

    try:
        url = 'http://www.anagramica.com/best/:' + str(letters)
        response = requests.get(url)
        data = response.json()

        # Returned data for the word 'ocean' is in the following dictonary,
        # format where the key is always the word 'best':
        # {
        #   "best": [
        #     "canoe",
        #     "ocean"
        #   ]
        # }
    except:
        pass

    return data

anagram_file = "anagrams.json"

def get_anagram_dict():

    with open(anagram_file, 'r') as file_handle:
        json_data = json.load(file_handle)

    return json_data

class Anagram(tk.Tk):

    def __init__(self):
        super().__init__()

        self.guesses = 5
        self.word_list = read_words_file()

        self.random_word, self.anagrams = self.get_new_word()

        self.label = tk.Label(self, text='Guess the ' + str(len(self.anagrams)) + ' anagrams for the word: ')
        self.label.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

        self.word_label = tk.Label(self, text=self.random_word)
        self.word_label.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.5)

        self.restart_button = tk.Button(self, bg='light gray', text='Get New Word!')
        self.restart_button.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.5)

        self.guess_remaining_label = tk.Label(self, text='Guesses remaining: ' + str(self.guesses))
        self.guess_remaining_label.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)

        self.entry_guess = tk.Entry(self)
        self.entry_guess.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

        self.entry_guess.bind('<KeyPress>', self.on_guess)
        self.restart_button.bind('<ButtonPress>', self.restart)

    def restart(self, event):
        if self.anagrams is not None:
            messagebox.showinfo('Answers', 'The anagrams were: ' + repr(self.anagrams))

        self.random_word, self.anagrams = self.get_new_word()
        self.guesses = 5
        self.guess_remaining_label.configure(text='Guesses remaining: ' + str(self.guesses))
        self.word_label.configure(text=self.random_word)

    def get_new_word(self):
        data = get_anagram_dict()
        random_word = random.choice(list(data.keys()))
        anagrams = data[random_word]

        return random_word, anagrams

    def on_guess(self, event):
        key = str(event.keysym)

        if key.lower() == 'return':
            word_guessed = self.entry_guess.get()

            if word_guessed != self.random_word and word_guessed in self.anagrams:
                print(self.anagrams)
            else:
                self.guesses -= 1
                self.guess_remaining_label.configure(text='Guesses remaining: ' + str(self.guesses))
                messagebox.showerror('', 'INCORRECT!')

                if self.guesses == 0:
                    print(self.anagram.values())

if __name__ == '__main__':
    #generate_file()

    game = Anagram()
    game.title('League Anagram Game')
    game.geometry('400x50')
    game.mainloop()
