class PigLatinConverter:

    @staticmethod
    def pig_word(word):
        split = PigLatinConverter.first_vowel(word)
        if split == 0:
            return word + '-hay'
        return word[split:] + '-' + word[0:split] + 'ay'

    @staticmethod
    def translate(s):
        latin = ""
        i = 0

        while i < len(s):

            # Take care of punctuation and spaces
            while i < len(s) and not s[i].isalpha():
                latin = latin + s[i]
                i += 1

            # If there aren't any words left, stop.
            if i >= len(s):
                break

            # Otherwise we're at the beginning of a word.
            begin = i
            while i < len(s) and s[i].isalpha():
                i += 1

            # Now we're at the end of a word, so translate it.
            end = i
            word_to_translate = s[begin : end]
            latin = latin + PigLatinConverter.pig_word(word_to_translate)

        return latin

    @staticmethod
    def first_vowel(word):
        word = word.lower()

        vowels = ['a', 'e', 'i', 'o', 'u']

        for i, letter in enumerate(word):
            if letter in vowels:
                return i

        return 0
