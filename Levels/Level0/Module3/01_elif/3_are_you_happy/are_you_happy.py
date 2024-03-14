from tkinter import Tk, simpledialog, messagebox


# TODO: Look at the AreYouHappy.png image
#       In this lesson we will use pop-ups to recreate the chart using if and elif statements


# Create a Tkinter window
root = Tk()  # ;
root.withdraw()  # ;

# Ask the user if they are happy
answer = simpledialog.askstring("Question", "Are you happy? (yes/no)")  # ;

# Check the user's response and provide a follow-up questions with nested if/elif/else statements
if answer:  # ;
    if answer.lower() == "yes":  # ;
        follow_up = simpledialog.askstring(
            "Question", "That's great! What made you happy?"
        )  # ;
        messagebox.showinfo(
            "Response", f"I'm glad you're happy because of {follow_up}."  # ;
        )  # ;
    elif answer.lower() == "no":
        follow_up = simpledialog.askstring(
            "Question", "I'm sorry to hear that. Can I help?"
        )
        if follow_up and follow_up.lower() == "yes":  # ;
            messagebox.showinfo(
                "Response", "I'm here to help if you need anything."  # ;
            )  # ;
        else:  # ;
            messagebox.showinfo(
                "Response", "Okay, let me know if you change your mind."  # ;
            )  # ;
    else:  # ;
        messagebox.showinfo("Response", "Please answer with 'yes' or 'no'.")  # ;
else:  # ;
    messagebox.showinfo("Response", "No input received. Goodbye!")  # ;

# Run the window's .mainloop() method
root.mainloop()  # ;
