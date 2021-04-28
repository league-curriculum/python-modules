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
        self.assertEqual("x_x_x_x_x_x_x_underscores_x_x_x_x_x_x",
                         function("x x x x x x x underscores x x x x x x"))

    def test_line_leader(self):
        function = _b_string_methods.line_leader
        self.assertEqual('John A', function("John C", "John B", "John A"))
        self.assertEqual('John A', function(" John C   ", "     John B ", "           John A  "))
        self.assertEqual('Charley F', function("  Allison Z", " Brad H ", " Charley F "))

    def test_numeral_sum(self):
        function = _b_string_methods.numeral_sum
        self.assertEqual(0, function(''))
        self.assertEqual(5, function('11111'))
        self.assertEqual(3, function('a1b2c'))
        self.assertEqual(45, function('x1x2x3x4x5x6x7x8x9x'))

    def test_substring_count(self):
        function = _b_string_methods.substring_count
        self.assertEqual(3, function("subsubsub", "sub"))
        self.assertEqual(2, function("s ubsubsu bsubs ub", "sub"))
        self.assertEqual(3, function("Here I'm counting spaces"," "))
        self.assertEqual(0, function("There shouldn't be matches here", "tuna"))

    def test_words_end_with_substring(self):
        function = _b_string_methods.words_ends_with_substring
        self.assertEqual(3, function("He quietly and slowly backed away from the bear that was hungrily looking at him", "ly"))
        self.assertEqual(2, function("He was visiting The League of Amazing Programmers.", "ing"))
        self.assertEqual(7, function("Here are multiple words that have the same letter at the end.", "e"))
        self.assertEqual(0, function("This should give us zero matches", "lemonade"))

    def test_distance(self):
        function = _b_string_methods.distance
        self.assertEqual(6, function("subsubsubsub", "sub"))
        self.assertEqual(7, function("subsubsubsub", "ub"))
        self.assertEqual(28, function("The League The Le ague TheLeag ue The League", "League"))
        self.assertEqual(0, function("bb", "b"))

    def test_palindrome(self):
        function = _b_string_methods.palindrome
        self.assertTrue(function('ABA'))
        self.assertTrue(function('ABBA'))
        self.assertTrue(function('racecar'))
        self.assertTrue(function('Was it a cat I saw?'))
        self.assertTrue(function('A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal – Panama'))
        self.assertTrue(function('Doc, Note: I Dissent. A Fast Never Prevents A Fatness. I Diet On Cod.'))
        self.assertFalse(function('abcdefghijklmnopqrstuvwxyz'))
        self.assertFalse(function('This is not a palindrome'))
        self.assertFalse(function('This is close but not quite right etiuq ton tub esolc si sihT'))


if __name__ == '__main__':
    unittest.main()
