import unittest
import _b_string_methods

# TODO Run this file and check if your function implementations in the
#   string methods file pass all the tests below!


class StringTests(unittest.TestCase):

    def test_find_longer_string(self):
        function = _b_string_methods.find_longer_string
        self.assertEqual('A', function('', 'A'))
        self.assertEqual('A', function('A', ''))
        self.assertEqual('equal', function('equal', 'equal'))

    def test_format_spaces(self):
        function = _b_string_methods.format_spaces
        self.assertEqual("This String should not change", function("This String should not change"))
        self.assertEqual("This_String_should_have_its_spaces_filled_with_underscores",
                         function("This String should have its spaces filled with underscores"))

    def test_substring_count(self):
        function = _b_string_methods.substring_count
        self.assertEqual(3, function("subsubsub", "sub"))
        self.assertEqual(0, function("There shouldn't be matches here", "tuna"))

    def test_palindrome(self):
        function = _b_string_methods.palindrome
        self.assertTrue(function('ABA'))
        self.assertTrue(function('ABBA'))
        self.assertTrue(function('racecar'))
        self.assertFalse(function('abcdefghijklmnopqrstuvwxyz'))
        self.assertFalse(function('This is not a palindrome'))


if __name__ == '__main__':
    unittest.main()
