from tkinter import simpledialog, messagebox, Tk

import vlc, pafy
######################### TODO NEED TO FIGURE OUT VLC IMPORT
def play_video(url):
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)
    media.play()

if __name__ == '__main__':

    # TODO 1) Make a new window variable, window = Tk()
    #      2) Hide the window using the window's .withdraw() method
    #      3) Ask the user how many cats they have
    #      4) If they have 3 or more cats, tell them they are a crazy cat lady
    #      5) If they have less than 3 cats AND more than 0 cats, call the method below to show them a cat video
    #      6) If they have 0 cats, show them a video of A Frog Sitting on a Bench Like a Human

    window = Tk()
    window.withdraw()

    num_cats = simpledialog.askstring(title="Question", prompt="How many cats do you have?")

    if num_cats >= "3":
        messagebox.showinfo(message="You are a crazy cat lady")
    elif "3" > num_cats > "0":
        play_video("https://www.youtube.com/watch?v=hY7m5jjJ9mM")
    elif num_cats == "0":
        play_video("https://www.youtube.com/watch?v=oj_yLBltPE8")