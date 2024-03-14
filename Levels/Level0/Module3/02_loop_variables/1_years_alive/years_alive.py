# TODO 1) Use a for loop to print out all of the years you have been alive.  Use the range function to loop through the years starting at the year you were born end ending at the current year.  There may be some slight differneces depending if you have or have not already had your birthday this year, adjust the years in the range function to make it more accurate.
# TODO 2) Create a variable named age and set it to 0, in the for loop increment the age variable by 1 each time the loop runs.  Print out the age variable each time the loop runs.

age = 0  # ;
for i in range(1978, 2024):  # ;
    print(f"Year: {i}, I turned {age} years old")  # ;
    age += 1  # ;
