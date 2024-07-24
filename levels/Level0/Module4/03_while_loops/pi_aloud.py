"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math



pass
window = Tk()
window.withdraw()
# TODO) Place the first 20 digits of pi into a String variable.
#  3.1415926535897932384
pi_str = '3.1415926535897932384'

# TODO) Print out the first 3 digits of pi. For example,
#  pi_str[0]   # first digit
#  pi_str[1]   # second digit
print(pi_str[0])
print(pi_str[1])
print(pi_str[2])
print(pi_str[3])

# TODO) Use a while loop to keep asking for the next digit of pi
pi_digit_index = 4
while True:
    # TODO) If they are correct, print "correct".
    #  If they are not, print "incorrect" and break out of the while loop
    answer = simpledialog.askstring(None, 'What is digit #' + str(pi_digit_index) + ' of pi?')

    if answer == pi_str[pi_digit_index]:
        pi_digit_index += 1
        messagebox.showinfo(None, 'Correct!')
    else:
        messagebox.showinfo(None, 'Incorrect, it was ' + pi_str[pi_digit_index])
        break

# TODO) Print out how many digits of pi the user was able to recite
#  in a row
messagebox.showinfo('Results', 'You got ' + str(pi_digit_index - 4) + ' digits of pi correct!')
