from tkinter import simpledialog, Tk

can_play_sounds = False


def play_mister_zee():
    if can_play_sounds:
        # TODO FIGURE OUT SOUND
        x = 0
    else:
        print("Mister Zee requires shiny objects")


def many_shiny_objects():
    # TODO 1) Call the method above to play Mister Zee
    play_mister_zee()
    # TODO 2) Ask the user how many shiny objects they want
    shiny = simpledialog.askstring(title="Question", prompt="How many shiny objects do you want?")
    # TODO 3) Play the sound that many times
    for i in range(int(shiny)):
        play_mister_zee()

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    many_shiny_objects()

############# Use this method. DON'T CHANGE THE CODE BELOW #############
