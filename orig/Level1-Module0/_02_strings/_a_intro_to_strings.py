"""
Below is a demo of how to use different string methods in Python
For a complete reference:
https://docs.python.org/3/library/string.html
"""

# No code needs to be written in this file. Use it as a reference for the
# following projects.

if __name__ == '__main__':

    # Declaring and initializing a string variable
    new_str = "Welcome to Python!"

    # Getting the number of characters in a string
    num_characters = len(new_str)

    # Getting a character from a string by index--similar to lists
    character = new_str[2]  # 'l'
    print(character)

    # Check if a character is a letter or a number
    print('Is ' + new_str[2] + ' a letter: ' + str(new_str[2].isalpha()))
    print('Is ' + new_str[2] + ' a digit: ' + str(new_str[2].isdigit()))

    # Removing leading and trailing whitespace from a string
    whitespace_str = '   This string has whitespace   '
    print('original string .......: ' + whitespace_str + ' ' + str(len(whitespace_str)))
    print('leading spaces removed : ' + whitespace_str.lstrip() + ' ' + str(len(whitespace_str.lstrip())))
    print('trailing spaces removed: ' + whitespace_str.rstrip() + ' ' + str(len(whitespace_str.rstrip())))
    print('leading and trailing spaces removed: ' + whitespace_str.strip() + ' ' + str(len(whitespace_str.strip())))

    # Find the number of times a substring (or letter) appears in a string
    num_character = new_str.count('o')      # 3 occurrences
    num_substring = new_str.count('to')     # 1 occurrences
    print('\'o\' occurs ' + str(num_character) + ' times')
    print('\'to\' occurs ' + str(num_substring) + ' times')

    # Making a copy of a string
    str_copy = new_str[:]

    # Convert string to all upper case or lower case
    print(str_copy.upper())
    print(str_copy.lower())
    print(new_str)

    # Getting a substring from a string [<stat>:<end>], <end> is NOT inclusive
    new_substring1 = new_str[0:7]   # 'Welcome'
    new_substring2 = new_str[8:10]  # 'to
    new_substring3 = new_str[11:]   # 'Python!'
    print(new_substring1)
    print(new_substring2)
    print(new_substring3)

    # Finding the index of the first matching character or substring
    index = new_str.find('o')
    print('\'o\' 1st appearance at index: ' + str(index))
    index = new_str.find('o', index+1)
    print('\'o\' 2nd appearance at index: ' + str(index))

    # Converting a string to a list
    new_str_list = list(new_str)
    print(new_str_list)

    # Converting a list to a string
    back_to_string = ''.join(new_str_list)
    print(back_to_string)

    # Converting a list to a string with a separator (delimiter)
    back_to_string = '_'.join(new_str_list)
    print(back_to_string)

    # Replacing characters from a string
    back_to_string = back_to_string.replace('_', '')
    print(back_to_string)

    # Splitting a string into a list of strings separated by a space ' '
    split_str_list = new_str.split(' ')
    print(split_str_list)
