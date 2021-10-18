"""
Demo of File Input and Output
https://docs.python.org/3/library/functions.html#open
https://realpython.com/python-pathlib/
"""
# READING
# Data from files can be read into a Python program using Python's built-in
# 'open' function and 'with' keyword. Here is an example:
#
#   with open(file="test_file.txt", mode='r') as file_handle:
#       for line in file_handle:
#           print(line, end='')
#
# file="test_file.txt
#       Specifies the file name to open. Python looks for the file starting
#       from the directory that's executing the code (this file).
# mode='r'
#       Opens the file for reading operations only. Files can be opened with
#       different modes, see the writing section below.
# for line in file_handle:
#       'file_handle' is the variable representing the opened file. It can be
#       used to Iterate through each line in the file, starting from the top,
#       including the new-line characters at the end of each line. This is why
#       the print function has end=''. Without it there would be two new-lines
#       at the end of each line and the output would look double-spaced.
#
# WRITING
# Data can also be written into a file from a Python program. Here is an
# example:
#
#   with open(file="new_file.txt", mode='w') as file_handle:
#       file_handle.write("Writing to a file!")
#
# Notice the mode='w' is changed from 'r' to 'w'. Here are examples of the
# different modes:
#   mode='r' open for reading (default)
#   mode='w' open for writing, overwrites file if it exists
#   mode='x' open for writing, does NOT overwrite file if it exists
#   mode='a' open for writing to the end of the file, create new file if it does not exist
#   mode='r+' open for updating (reading and then writing)
#   mode='w+' open for updating (writing and then reading)
from pathlib import Path
from datetime import datetime

if __name__ == '__main__':
    filename = "test_file.txt"
    filename_2 = "test_file_different_directory.txt"
    filename_3 = 'new_file.txt'

    #
    # How to read a file
    #
    with open(file=filename, mode='r') as file_handle:
        print('1. Reading ' + str(filename))
        for line in file_handle:
            print(line, end='')

    #
    # How to read a file in another directory
    #
    print('\n')

    # Path.cwd() is short for Current Working Directory (cwd), the directory
    # containing the file that's being executed (Level2-Module0).
    file_path = Path.joinpath(Path.cwd(), 'text_files/test_directory', filename_2)

    with open(file=file_path, mode='r') as file_handle:
        print('2. Reading ' + str(file_path))
        for line in file_handle:
            print(line, end='')

    #
    # How create a new file in a different directory (mode='w')
    #
    print()
    file_path = Path.joinpath(Path.cwd(), 'text_files/test_directory', filename_3)
    with open(file=file_path, mode='w') as file_handle:
        cur_time = str(datetime.now())
        print('3. Writing new file ' + cur_time + ' to ' + str(file_path))
        file_handle.write("Writing new file " + cur_time + '\n')

    #
    # How to overwrite a file (mode='w')
    #
    print()
    with open(file=filename, mode='w') as file_handle:
        cur_time = str(datetime.now())
        print('4. Writing ' + cur_time + ' to ' + filename)
        file_handle.write("Writing " + cur_time + '\n')

    #
    # How to write to the end of an existing file. (mode='a')
    # Create new file if it does not exist.
    #
    print()
    with open(file=filename, mode='a') as file_handle:
        cur_time = str(datetime.now())
        print('5. Appending ' + cur_time + ' to ' + filename)
        file_handle.write("Appending/Adding " + cur_time)

    #
    # Check if a file exists using is_file()
    #
    print()
    path = Path(filename)
    file_exists = path.is_file()
    print('Is ' + str(path) + ' a file ...: ' + str(file_exists))

    path = Path('unknown_file.txt')
    file_exists = path.is_file()
    print('Is ' + str(path) + ' a file ...: ' + str(file_exists))

    path = Path.joinpath(Path.cwd(), 'text_files/test_directory', filename_2)
    file_exists = path.is_file()
    print('Is ' + str(path) + ' a file ...: ' + str(file_exists))

    path = Path.joinpath(Path.cwd(), 'text_files', 'unknown_file.txt')
    file_exists = path.is_file()
    print('Is ' + str(path) + ' a file ...: ' + str(file_exists))

    path = Path.joinpath(Path.cwd(), 'text_files/test_directory', filename_3)
    file_exists = path.is_file()
    print('Is ' + str(path) + ' a file ...: ' + str(file_exists))
