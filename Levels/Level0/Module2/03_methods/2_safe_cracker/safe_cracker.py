import random
import os
from tkinter import messagebox, Tk
import simpleaudio as sa


can_play_sounds = True
wekncrzpasfdkjhcfjse = random.randint(0, 99)


def crack_the_safe():
    # TODO: Your mission: Use the try_code method to crack the safe
    #  by trying all possible combinations
    # Study the try_code method to understand how it works and use it to crack the safe
    for i in range(9999900, 9999999):  # ;
        try_code(i)  # ;


def try_code(guess):
    print("trying" + str(guess))

    secret_code = 9999999 - wekncrzpasfdkjhcfjse

    if guess == secret_code:
        play_the_sound_of_success("me-gusta.wav").play()
        messagebox.showinfo(
            None, "Congratulations! You cracked the safe with " + str(guess)
        )

        # sys.exit(0)


def play_the_sound_of_success(file):
    file_path = os.path.join(os.path.dirname(__file__), file)
    return sa.WaveObject.from_wave_file(file_path)


window = Tk()
window.withdraw()
crack_the_safe()
