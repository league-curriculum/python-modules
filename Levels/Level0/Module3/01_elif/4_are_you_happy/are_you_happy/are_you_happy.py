from tkinter import Tk, simpledialog, messagebox


# TODO: Look at the AreYouHappy.png image
#       Use pop-ups to recreate the chart using if and elif statements
window = Tk()
window.withdraw()

happy = simpledialog.askstring(title="Question", prompt="Are you happy?")
if happy == "yes":
    messagebox.showinfo(message="Keep doing whatever you're doing")
elif happy == "no":
    want = simpledialog.askstring(title="Question", prompt="Do you want to be happy?")
    if want == "yes":
        messagebox.showinfo(message="Change something")
    elif want == "no":
        messagebox.showinfo(message="Keep doing whatever you're doing")