"""
In this exercise, you will write a function that sings the song "99 Bottles of Rootbeer on the Wall". The song goes as follows: "99 bottles of rootbeer on the wall, 99 bottles of rootbeer. Take one down and pass it around, 98 bottles of rootbeer on the wall." The song continues until there are no more bottles of rootbeer on the wall. The last line of the song is "No more bottles of rootbeer on the wall, no more bottles of rootbeer. Go to the store and buy some more, 99 bottles of rootbeer on the wall." 
"""

# TODO 1) Create a function called sing_99_bottles.
# TODO 2) Use a for loop to sing the song.  The song should start with 99 bottles and end with no more bottles.  The song should be printed to the console.
# TODO 2.1) Do not write any print statements outside of the function.  All of the print statements should be inside the function.  Remember to handle the final line of the song slightly differnetly than the 99 count down lines. Hint:  There is a special character in python that will print a new line:  "/n"


def sing_99_bottles():  # ;
    for num in range(99, 0, -1):  # ;
        if num == 1:  # ;
            bottle = "bottle"  # ;
            next_bottle = "no more bottles"  # ;
        else:  # ;
            bottle = "bottles"  # ;
            next_bottle = str(num - 1) + " bottles"  # ;

        print(
            f"{num} {bottle} of rootbeer on the wall, {num} {bottle} of rootbeer."
        )  # ;
        print(
            f"Take one down and pass it around, {next_bottle} of rootbeer on the wall.\n"
        )  # ;

    print("No more bottles of rootbeer on the wall, no more bottles of rootbeer.")  # ;
    print("Go to the store and buy some more, 99 bottles of rootbeer on the wall.")  # ;


# TODO 3) Call the sing_99_bottles function
sing_99_bottles()  # ;
