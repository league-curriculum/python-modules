from tkinter import simpledialog, Tk
import simpleaudio as sa
import os
import time

# If simpleaudio is not installed, you can install it by running the following command in the terminal: pip install simpleaudio or pip3 install simpleaudio if running on unix/linux.  Otherwise set can_play_sounds to False.
can_play_sounds = True


# This method will play a sound file, it takes the file name as a parameter. Do not modify this method.
def get_and_play_audio_file(file):
    file_path = os.path.join(os.path.dirname(__file__), file)
    return sa.WaveObject.from_wave_file(file_path).play()


# This Function is the function you will call to play the sound in the instructions below.
def play_mister_zee():
    if can_play_sounds:
        get_and_play_audio_file("shiny.wav")
    else:
        simpledialog.showinfo("Message", "Shiny object sound not available.")


# TODO 1) Create a function called many_shiny_objects that will play the sound of Mister Zee and ask the user how many shiny objects they want. Then play the sound that many times.
def many_shiny_objects():  # ;

    # TODO 1) Ask the user how many shiny objects they want using the simpledialog.askstring method
    shiny = simpledialog.askstring(  # ;
        title="Question", prompt="How many shiny objects do you want?"  # ;
    )
    # TODO 3) Play the sound that many times using a for loop.  You will need to convert the string to an integer using the int() function.
    for i in range(int(shiny)):  # ;
        # TODO 2) Call the time function to wait for 1 second: time.sleep(1)  So that the sounds do not play too quickly.
        time.sleep(1)  # ;
        play_mister_zee()  # ;


# TODO 4) Create a window: window = Tk() and then hide the window: window.withdraw()
# TODO 5) Call the many_shiny_objects function
window = Tk()  # ;
window.withdraw()  # ;
many_shiny_objects()  # ;
