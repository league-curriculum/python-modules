# TODO: Create a simple adventure story using input and output dialogs. The story should have at least three different paths and outcomes based on the player's choices. Use if, elif, and else statements to check the player's choices and display different messages based on the outcomes. You can use the get_input and show_message functions to display input and output dialogs. You can also use the random.choice function to generate random outcomes for the story. Be creative and have fun with the adventure story!

# TODO: You can refer back to previous lessons for what you need to import and how to use functions, methods, loops, if/else/elif statements, etc.

# TODO:  Rememer to create a window and withdraw and run the mainloop at the end of the program.

import tkinter as tk  # ;
from tkinter import simpledialog, messagebox  # ;
import random  # ;


# Function to display a pop-up dialog and return the user's input#;
def get_input(prompt):  # ;
    return simpledialog.askstring("Adventure Story", prompt)  # ;


# Function to display a pop-up dialog with a message#;
def show_message(message):  # ;
    messagebox.showinfo("Adventure Story", message)  # ;


# Function to play the adventure story#;
def play_adventure_story():  # ;
    # Display an introduction and ask for the player's name#;
    player_name = get_input("Welcome to the Adventure Story! What is your name?")  # ;

    # Check if the player entered a name# ;
    if player_name:  # ;
        show_message(f"Hello, {player_name}! Let's embark on an adventure.")  # ;

        # Start the adventure# ;
        show_message(  # ;
            "You wake up in a mysterious forest. Do you want to go left, right, or straight ahead?"  # ;
        )  # ;

        # Loop until the player makes a valid choice# ;
        while True:  # ;
            direction = get_input("Enter 'left', 'right', or 'straight':")  # ;
            if direction in ["left", "right", "straight"]:  # ;
                break  # ;
            else:  # ;
                show_message("Please enter 'left', 'right', or 'straight'.")  # ;

        # Check the player's choice and continue the adventure# ;
        if direction == "left":  # ;
            show_message("You encounter a friendly squirrel.")  # ;
            # Ask the player if they want to feed the squirrel# ;
            feed_squirrel = get_input(  # ;
                "The squirrel seems hungry. Do you want to feed it? (yes/no)"  # ;
            )  # ;
            if feed_squirrel.lower() == "yes":  # ;
                show_message(  # ;
                    "The squirrel happily accepts your offer and guides you deeper into the forest."  # ;
                )  # ;
            else:  # ;
                show_message(  # ;
                    "The squirrel looks disappointed but leads you deeper into the forest anyway."  # ;
                )  # ;

            # Continue the adventure# ;
            show_message(
                "You come across a hidden cave. Do you want to explore it?"
            )  # ;
            explore_cave = get_input(  # ;
                "Enter 'yes' to explore the cave, or 'no' to continue your journey:"  # ;
            )  # ;
            if explore_cave.lower() == "yes":  # ;
                show_message("You enter the cave and find a treasure chest!")  # ;
            else:  # ;
                show_message(  # ;
                    "You decide not to enter the cave and continue your journey."  # ;
                )  # ;

        elif direction == "right":  # ;
            show_message("You find an abandoned cabin.")  # ;
            # Ask the player if they want to explore the cabin# ;
            explore_cabin = get_input("Do you want to explore the cabin? (yes/no)")  # ;
            if explore_cabin.lower() == "yes":  # ;
                show_message("You enter the cabin and find some supplies.")  # ;
            else:  # ;
                show_message(
                    "You decide to leave the cabin and continue exploring."
                )  # ;

            # Continue the adventure# ;
            show_message("You stumble upon a river. Do you want to cross it?")  # ;
            cross_river = get_input(  # ;
                "Enter 'yes' to cross the river, or 'no' to find another path:"  # ;
            )  # ;
            if cross_river.lower() == "yes":  # ;
                show_message(  # ;
                    "You successfully cross the river and continue your journey."  # ;
                )  # ;
            else:  # ;
                show_message("You find another path and continue exploring.")  # ;

        else:  # ;
            show_message("You come across a magical pond.")  # ;
            # Ask the player if they want to swim in the pond# ;
            swim_pond = get_input("Do you want to swim in the pond? (yes/no)")  # ;
            if swim_pond.lower() == "yes":  # ;
                # Generate a random outcome for swimming in the pond# ;
                outcome = random.choice(  # ;
                    [  # ;
                        "You feel refreshed and energized!",  # ;
                        "You discover hidden treasure at the bottom!",  # ;
                        "You encounter a water spirit and receive a mysterious gift.",  # ;
                    ]  # ;
                )  # ;
                show_message(outcome)  # ;
            else:  # ;
                show_message(
                    "You decide to avoid the pond and continue your journey."
                )  # ;

            # Continue the adventure# ;
            show_message(
                "You encounter a fork in the road. Which path do you choose?"
            )  # ;
            fork_path = get_input("Enter 'left' or 'right' to choose a path:")  # ;
            if fork_path.lower() == "left":  # ;
                show_message(
                    "You follow the left path and find a beautiful waterfall."
                )  # ;
            else:  # ;
                show_message(
                    "You follow the right path and discover an ancient ruin."
                )  # ;

        # End of the adventure# ;
        show_message("The adventure has come to an end. Thanks for playing!")  # ;
    else:  # ;
        show_message("No name entered. Goodbye!")  # ;


# Create a Tkinter window# ;
root = tk.Tk()  # ;
root.withdraw()  # ;

# Start the adventure story# ;
play_adventure_story()  # ;

# Close the Tkinter window# ;
root.mainloop()  # ;
