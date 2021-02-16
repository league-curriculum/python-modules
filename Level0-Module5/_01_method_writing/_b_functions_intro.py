"""
Write the function definitions for the function calls below
"""
from tkinter import messagebox, simpledialog, Tk
import random
import unittest


# TODO Write function definitions below!


class FunctionTests(unittest.TestCase):

    # TODO 1) Write a function definition for multiply
    def test_1(self):
        self.assertEqual(100, multiply(10, 10))

    # TODO 2) Write a function definition for str_cat
    def test_2(self):
        self.assertEqual('Welcome to Python', str_cat(var1='Welcome', var2='to', var3='Python'))

    # TODO 3) Write a function definition for greater_than
    def test_3(self):
        self.assertEqual(True, greater_than(1, 2))

    # TODO 4) Write a function definition for get_random_number
    def test_4(self):
        for i in range(100):
            random_number = get_random_number(low=0, high=100)

            if random_number < 0 or random_number > 100:
                self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
