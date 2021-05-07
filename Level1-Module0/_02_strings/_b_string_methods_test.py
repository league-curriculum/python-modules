"""
String methods: Create the necessary functions to make the tests pass
"""
import unittest

# TODO: 1) Implement the functions below so that the test cases in the string
#  methods test file pass. You can delete the 'pass' instruction.
#
# TODO: 2) Run the string test file. A summary of the test results on your
#  code will be displayed. Fix any problems in your code so that all the
#  tests pass.

# Given Strings s1 and s2, return the longer String
def find_longer_string(s1, s2):
    # Longer way
    if len(s1) > len(s2):
        return s1
    elif len(s1) < len(s2):
        return s2
    return 'equal'

    # Shorter way
    #if len(s1) == len(s2):
    #    return 'equal'
    #return s1 if len(s1) > len(s2) else s2


# If String s contains the word "underscores", change all of the spaces to
# underscores
def format_spaces(s1):
    if 'underscores' in s1:
        s1 = s1.replace(' ', '_')

    return s1


# Return the number of times String substring appears in String s
def substring_count(s, substring):
    return s.count(substring)


# Return true if String s is a palindrome
# palindromes are words or phrases are read the same forward as backward.
def palindrome(s):
    for i in range(len(s)):
        if s[i] != s[-1 - i]:
            return False

    return True

# ======================= DO NOT EDIT THE CODE BELOW =========================

class StringTests(unittest.TestCase):

    def test_find_longer_string(self):
        function = find_longer_string
        self.assertEqual('A', function('', 'A'))
        self.assertEqual('A', function('A', ''))
        self.assertEqual('equal', function('equal', 'equal'))

    def test_format_spaces(self):
        function = format_spaces
        self.assertEqual("This String should not change", function("This String should not change"))
        self.assertEqual("This_String_should_have_its_spaces_filled_with_underscores",
                         function("This String should have its spaces filled with underscores"))

    def test_substring_count(self):
        function = substring_count
        self.assertEqual(3, function("subsubsub", "sub"))
        self.assertEqual(0, function("There shouldn't be matches here", "tuna"))

    def test_palindrome(self):
        function = palindrome
        self.assertTrue(function('ABA'))
        self.assertTrue(function('ABBA'))
        self.assertTrue(function('racecar'))
        self.assertFalse(function('abcdefghijklmnopqrstuvwxyz'))
        self.assertFalse(function('This is not a palindrome'))


if __name__ == '__main__':
    unittest.main()
