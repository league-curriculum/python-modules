import unittest
import _b_string_methods


class StringTests(unittest.TestCase):

    def test_find_longer_string(self):
        method = _b_string_methods.find_longer_string
        self.assertEqual('A', method('', 'A'))
        self.assertEqual('A', method('A', ''))
        self.assertEqual('equal', method('equal', 'equal'))

    def test_format_spaces(self):
        method = _b_string_methods.format_spaces
        self.assertEqual("This String should not change", method("This String should not change"))
        self.assertEqual("This_String_should_have_its_spaces_filled_with_underscores",
                         method("This String should have its spaces filled with underscores"))
        self.assertEqual("x_x_x_x_x_x_x_underscores_x_x_x_x_x_x",
                         method("x x x x x x x underscores x x x x x x"))

    def test_line_leader(self):
        method = _b_string_methods.line_leader
        self.assertEqual('John A', method("John C", "John B", "John A"))
        self.assertEqual('John A', method(" John C   ", "     John B ", "           John A  "))
        self.assertEqual('Charley F', method("  Allison Z", " Brad H ", " Charley F "))

    def test_numeral_sum(self):
        method = _b_string_methods.numeral_sum
        self.assertEqual(0, method(''))
        self.assertEqual(5, method('11111'))
        self.assertEqual(3, method('a1b2c'))
        self.assertEqual(45, method('x1x2x3x4x5x6x7x8x9x'))

    def test_substring_count(self):
        method = _b_string_methods.substring_count
        self.assertEqual(3, method("subsubsub", "sub"))
        self.assertEqual(2, method("s ubsubsu bsubs ub", "sub"))
        self.assertEqual(3, method("Here I'm counting spaces"," "))
        self.assertEqual(0, method("There shouldn't be matches here", "tuna"))

    def test_words_end_with_substring(self):
        method = _b_string_methods.words_ends_with_substring
        self.assertEqual(3, method("He quietly and slowly backed away from the bear that was hungrily looking at him", "ly"))
        self.assertEqual(2, method("He was visiting The League of Amazing Programmers.", "ing"))
        self.assertEqual(7, method("Here are multiple words that have the same letter at the end.", "e"))
        self.assertEqual(0, method("This should give us zero matches", "lemonade"))

    def test_distance(self):
        method = _b_string_methods.distance
        self.assertEqual(6, method("subsubsubsub", "sub"))
        self.assertEqual(7, method("subsubsubsub", "ub"))
        self.assertEqual(28, method("The League The Le ague TheLeag ue The League", "League"))
        self.assertEqual(0, method("bb", "b"))

    def test_palindrome(self):
        method = _b_string_methods.palindrome
        self.assertTrue(method('ABA'))
        self.assertTrue(method('ABBA'))
        self.assertTrue(method('racecar'))
        self.assertTrue(method('Was it a cat I saw?'))
        self.assertTrue(method('A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal – Panama'))
        self.assertTrue(method('Doc, Note: I Dissent. A Fast Never Prevents A Fatness. I Diet On Cod.'))
        self.assertFalse(method('abcdefghijklmnopqrstuvwxyz'))
        self.assertFalse(method('This is not a palindrome'))
        self.assertFalse(method('This is close but not quite right etiuq ton tub esolc si sihT'))


if __name__ == '__main__':
    unittest.main()
