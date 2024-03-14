import webbrowser
from tkinter import simpledialog, messagebox, Tk


# This function is used to play a video from a given URL. It uses the webbrowser module to open the URL in the default web browser. Do not modify this function.
def play_video(url):
    webbrowser.open(url)


# TODO 1) Make a new window variable, window = Tk()
#      2) Hide the window using the window's .withdraw() method
window = Tk()  # ;
window.withdraw()  # ;

# Crazy Cats Link:
crazy_cat = "https://youtu.be/lrajbjOPWjo?si=cyWzK3_NkYDSCzAI"

# Frog Link:
beach_frog = "https://www.youtube.com/watch?v=oj_yLBltPE8"

# TODO 3) Ask the user how many cats they have and save it to a variable called num_cats.  Hint: use simpledialog.askinteger
num_cats = simpledialog.askinteger(
    title="Question", prompt="How many cats do you have?"
)  # ;

# TODO 4) First we must check if the user input is not None.  Else, show a message box with the message "Invalid input. Please enter a valid number of cats."
#      5) Nested under the NONE check we will check If they have 3 or more cats, tell them they are a crazy cat lady
#     6) Elif they have less than 3 cats AND more than 0 cats, call the play_video function to show them a cat video
#    7) Elif they have 0 cats, show them a video of A Frog Sitting on a Bench Like a Human
if num_cats is not None:  # ;
    if num_cats >= 3:  # ;
        messagebox.showinfo(message="You are a crazy cat lady")  # ;
    elif 0 < num_cats < 3:  # ;
        play_video(crazy_cat)  # ;
    elif num_cats == 0:
        play_video(beach_frog)  # ;
else:  # ;
    messagebox.showinfo(
        message="Invalid input. Please enter a valid number of cats."
    )  # ;

# TODO 8) Run the window's .mainloop() method
window.mainloop()
