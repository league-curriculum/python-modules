"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk



# TODO)
#  1. Ask the user for a number
#  2. Use a for loop, if statement, and modulo to find if the number
#     is prime.
#  3. If the number is divisible by any number other than 1 or itself,
#     the number is not prime.
window = Tk()
window.withdraw()

number = simpledialog.askinteger(None, 'Enter a positive integer')

is_prime = True

for i in range(number):
    if i > 1 and number % i == 0:
        is_prime = False
        break

if is_prime:
    messagebox.showinfo(None, 'That number IS prime!')
else:
    messagebox.showinfo(None, 'That number IS NOT prime!')
