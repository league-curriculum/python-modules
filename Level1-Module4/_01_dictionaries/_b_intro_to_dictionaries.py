"""
Introduction to dictionaries
"""
import unittest

# TODO: Return a dictionary with 4 key-value pairs
def initialize_dictionary():

    return dict()

# TODO: Return a dictionary using the two input parameter lists.
#  The first element in both lists should be a key-value pair, same
#  for the second, etc. Assume both input parameters have the same length.
def initialize_dictionary_from_lists(keys, values):

    return dict()

# TODO: Return a dictionary with the specified key's value updated to the new
#  value. If the key does not exist in the dictionary, do not change the
#  dictionary.
def dictionary_update(dictionary, key, new_value):

    return dict()

# TODO: Return a dictionary with the input dictionary's keys and values
#  reversed.
def reverse_key_values(dictionary):

    return dict()

# TODO Return a dictionary containing the matching key-value pairs from
#  dict_1 and dict_2:
def dictionary_overlap(dict_1, dict_2):

    return dict()

# ======================= DO NOT EDIT THE CODE BELOW =========================

class DictionaryTests(unittest.TestCase):

    def test_initialize_dictionary(self):
        new_dict = initialize_dictionary()
        self.assertTrue(type(new_dict) is dict)
        self.assertEqual(4, len(new_dict))

    def test_initialize_dictionary_from_lists(self):
        keys = [91, 50, 120, 7, 0]
        values = ['John', 'Javier', 'Jessica', 'Janelle', 'Jamal' ]
        new_dictionary = initialize_dictionary_from_lists(keys, values)

        # Should have 5 entries
        self.assertEqual(5, len(new_dictionary))

        # Each key-value should be in sync
        for key, value in new_dictionary.items():
            try:
                index = keys.index(key)
                self.assertEqual(values[index], new_dictionary[key])
            except ValueError:
                print('ERROR: ' + str(key) + ' is not found in ' + str(keys))
                self.assertTrue(False)

    def test_dictionary_update(self):
        schedule = {'9a' : 'school', '1p' : 'lunch', '4p' : 'soccer practice', '6p' : 'dinner', '7p' : 'homework'}
        classes = {1 : 'English', 2 : 'Social Studies', 3 : 'Biology', 4 : 'Homeroom', 5 : 'Math', 6 : 'Music'}

        # Key exists, should update
        new_schedule = dictionary_update(schedule, '4p', 'cross country')
        new_classes = dictionary_update(classes, 3, 'Spanish')
        self.assertEqual(5, len(new_schedule))
        self.assertEqual(6, len(new_classes))
        self.assertEqual('cross country', new_schedule['4p'])
        self.assertEqual('Spanish', new_classes[3])

        # Key DOES NOT exists, should NOT update
        new_schedule = dictionary_update(schedule, 'INVALID KEY', 'SHOULD NOT UPDATE')
        new_classes = dictionary_update(classes, 7, 'SHOULD NOT UPDATE')
        self.assertEqual(5, len(new_schedule))
        self.assertEqual(6, len(new_classes))
        self.assertEqual('cross country', new_schedule['4p'])
        self.assertEqual('Spanish', new_classes[3])

    def test_reverse_key_values(self):
        original = {1 : 'English', 2 : 'Social Studies', 3 : 'Biology', 4 : 'Homeroom', 5 : 'Math', 6 : 'Music'}
        reverse = {'English' : 1, 'Social Studies' : 2, 'Biology' : 3, 'Homeroom' : 4, 'Math' : 5, 'Music' : 6}

        new_dict = reverse_key_values(original)

        self.assertEqual(len(reverse), len(new_dict))

        for key in new_dict:
            self.assertEqual(reverse[key], new_dict[key])

    def test_dictionary_overlap(self):
        dict_1 = {1 : 'English', 2 : 'Social Studies', 3 : 'Biology', 4 : 'Homeroom', 5 : 'Math', 6 : 'Programming'}
        dict_2 = {1 : 'Math', 2 : 'English', 3 : 'Art', 4 : 'Homeroom', 5 : 'French', 6 : 'Programming', 7 : 'PE'}
        overlap = {4 : 'Homeroom', 6 : 'Programming'}

        new_dict = dictionary_overlap(dict_1, dict_2)

        self.assertEqual(len(overlap), len(new_dict))

        for key in new_dict:
            self.assertEqual(overlap[key], new_dict[key])


if __name__ == '__main__':
    unittest.main()
