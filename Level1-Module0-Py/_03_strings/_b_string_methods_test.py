import unittest
import _b_string_methods


class MyTestCase(unittest.TestCase):

    def test_find_longer_string(self):
        self.assertEqual('A', _b_string_methods.find_longer_string('', 'A'))
        self.assertEqual('A', _b_string_methods.find_longer_string('A', ''))
        self.assertEqual('equal', _b_string_methods.find_longer_string('equal', 'equal'))

    def test_format_spaces(self):
        self.assertEqual("This String should not change", _b_string_methods.format_spaces("This String should not change"))
        self.assertEqual("This_String_should_have_its_spaces_filled_with_underscores", _b_string_methods.formatSpaces("This String should have its spaces filled with underscores"))
        self.assertEqual("x_x_x_x_x_x_x_underscores_x_x_x_x_x_x", _b_string_methods.format_spaces("x x x x x x x underscores x x x x x x"))

    def test_line_leader(self):
        self.assertEqual('John A', _b_string_methods.line_leader("John C", "John B", "John A"))
        self.assertEqual('John A', _b_string_methods.line_leader(" John C   ", "     John B ", "           John A  "))
        self.assertEqual('Charley F', _b_string_methods.line_leader("  Allison Z", " Brad H ", " Charley F "))

    def test_numeral_sum(self):
        self.assertEqual(0, _b_string_methods.numeral_sum(''))
        self.assertEqual(5, _b_string_methods.numeral_sum('11111'))
        self.assertEqual(3, _b_string_methods.numeral_sum('a1b2c'))
        self.assertEqual(45, _b_string_methods.numeral_sum('x1x2x3x4x5x6x7x8x9x'))

    def test_substring_count(self):
        self.assertEqual(3, _b_string_methods.substring_count("subsubsub", "sub"))
        self.assertEqual(2, _b_string_methods.substring_count("s ubsubsu bsubs ub", "sub"))
        self.assertEqual(3, _b_string_methods.substring_count("Here I'm counting spaces"," "))
        self.assertEqual(0, _b_string_methods.substring_count("There shouldn't be matches here", "tuna"))

    def test_words_end_with_substring(self):
        self.assertEqual(3, _b_string_methods.words_ends_with_substring("He quietly and slowly backed away from the bear that was hungrily looking at him", "ly"))
        self.assertEqual(2, _b_string_methods.words_ends_with_substring("He was visiting The League of Amazing Programmers.", "ing"))
        self.assertEqual(7, _b_string_methods.words_ends_with_substring("Here are multiple words that have the same letter at the end.", "e"))
        self.assertEqual(0, _b_string_methods.words_ends_with_substring("This should give us zero matches", "lemonade"))

    def test_distance(self):
        self.assertEqual(6, _b_string_methods.distance("subsubsubsub", "sub"))
        self.assertEqual(7, _b_string_methods.distance("subsubsubsub", "ub"))
        self.assertEqual(28, _b_string_methods.distance("The League The Le ague TheLeag ue The League", "League"))
        self.assertEqual(0, _b_string_methods.distance("bb", "b"))

    def test_palindrome(self):
        self.assertTrue(_b_string_methods.palindrome('ABA'))
        self.assertTrue(_b_string_methods.palindrome('ABBA'))
        self.assertTrue(_b_string_methods.palindrome('racecar'))
        self.assertTrue(_b_string_methods.palindrome('Was it a cat I saw?'))
        self.assertTrue(_b_string_methods.palindrome('A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal – Panama'))
        self.assertTrue(_b_string_methods.palindrome('Doc, Note: I Dissent. A Fast Never Prevents A Fatness. I Diet On Cod.'))
        self.assertFalse(_b_string_methods.palindrome('abcdefghijklmnopqrstuvwxyz'))
        self.assertFalse(_b_string_methods.palindrome('This is not a palendrome'))
        self.assertFalse(_b_string_methods.palindrome('This is close but not quite right etiuq ton tub esolc si sihT'))


if __name__ == '__main__':
    unittest.main()
