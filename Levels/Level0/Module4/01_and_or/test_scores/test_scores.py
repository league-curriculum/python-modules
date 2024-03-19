from tkinter import messagebox, simpledialog, Tk

# The teacher wants you to write a program that converts the score on 2
# 100 point tests to a letter grade. The teacher wants you to average the
# score from the 2 tests and print out the letter grade back to the user.
# The letter grades are assigned as follows:
#   A = 89.5 to 100
#   B = 79.5 to less than 89.5
#   C = 69.5 to less than 79.5
#   D = 59.5 to less than 69.5
#   F = less than 59.5

# TODO 1) Ask the user for their score on the FIRST test and store their score in a variable
first_test_score = simpledialog.askfloat(
    "First Test Score", "Enter your score on the FIRST test:"
)

# TODO 2) Ask the user for their score on the SECOND test and store their score in a variable
second_test_score = simpledialog.askfloat(
    "Second Test Score", "Enter your score on the SECOND test:"
)

# TODO 3) Check if the user entered a score for both tests, example: if score is not None: Else, set the score to 0 or any other default value you prefer
# TODO 4) Take the average score of both tests (total score / 2) and store it in a variable
if first_test_score is not None and second_test_score is not None:  # ;
    average_score = (first_test_score + second_test_score) / 2  # ;
else:  # ;
    average_score = 0.0  # ;

# TODO 5) Use if statements with 'and' and 'or' to check the average score
# TODO 6) For each score range save the corresponding letter grade and message in variables
if average_score >= 89.5:  # ;
    grade = "A"  # ;
    message = "Wow! You must have studied really hard for those tests!"  # ;
elif average_score >= 79.5 and average_score < 89.5:  # ;
    grade = "B"  # ;
    message = "Great job!"  # ;
elif average_score >= 69.5 and average_score < 79.5:  # ;
    grade = "C"  # ;
    message = "You're doing okay."  # ;
elif average_score >= 59.5 and average_score < 69.5:  # ;
    grade = "D"  # ;
    message = "You need to work harder."  # ;
else:  # ;
    grade = "F"  # ;
    message = "You need to study more."  # ;

# TODO 7) Display the letter grade and corresponding message to the user
messagebox.showinfo(  # ;
    "Letter Grade",  # ;
    f"Your average score is {average_score:.2f}, which#; corresponds to a(n) {grade}.\n{message}",
)  # ;
