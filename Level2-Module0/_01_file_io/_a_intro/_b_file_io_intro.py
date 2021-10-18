"""
Intro exercises for file input and output
"""
import unittest
import random
from pathlib import Path

# TODO 1) Read the filename and return a string containing the contents.
# Assume the file exists.
def reading_file(filename):
    return None

# TODO 2) Write the specified text to the given filename. If the file doesn't
#  exist the function should create it.
def write_file(filename, text):
    return None

# TODO 3) Return True if the filename exists at the given directory and return
#  False otherwise
def file_exists(directory_from_cwd, filename):
    return None


# ======================= DO NOT EDIT THE CODE BELOW =========================

class FileIOTests(unittest.TestCase):
    read_file_pass = False

    def test_reading_and_writing_file(self):
        filename = 'sample.txt'
        self.assertEqual('This is a sample text file\n', reading_file(filename))

        # Test below only runs if no failures/asserts above
        filename = 'test_writing_file.txt'
        rand_num = random.randint(0, 100)
        text = 'writing sample ' + str(rand_num)
        write_file(filename, text)

        self.assertEqual(text, reading_file(filename))

    def test_file_exists(self):
        filename = 'Alices_Adventures_In_Wonderland.txt'
        directory_from_cwd = 'text_files'

        self.assertTrue(file_exists(directory_from_cwd, filename))
        self.assertFalse(file_exists(directory_from_cwd, 'unknown.txt'))


if __name__ == '__main__':
    unittest.main()
