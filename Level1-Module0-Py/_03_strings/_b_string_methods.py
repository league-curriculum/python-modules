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


# If String s contains the word "underscores", change all of the spaces to underscores
def format_spaces(s1):
    if 'underscores' in s1:
        s1 = s1.replace(' ', '_')

    return s1


# Return the name of the person whose LAST name would appear first if they were
# in alphabetical order.
# You cannot assume there are no extra spaces around the name, but you can
# assume there is only one space between the first and last name.
# Strings can be compared alphabetically using <, >. Be aware that capital letters
# come first alphabetically:
# "abc" < "abd"   # True
# "abc" < "abD"   # False
def line_leader(s1, s2, s3):
    words = s1.strip().split(' ')
    last_name_1 = words[len(words) - 1]

    words = s2.strip().split(' ')
    last_name_2 = words[len(words) - 1]

    words = s3.strip().split(' ')
    last_name_3 = words[len(words) - 1]

    if last_name_1 < last_name_2 and last_name_1 < last_name_3:
        return s1.strip()

    if last_name_2 < last_name_1 and last_name_2 < last_name_3:
        return s2.strip()

    if last_name_3 < last_name_1 and last_name_3 < last_name_2:
        return s3.strip()

    return 'ERROR!!!'


# Return the sum of all numerical digits in the String
def numeral_sum(s):
    num_sum = 0

    for i in range(len(s)):
        if s[i].isdigit():
            num_sum += int(s[i])

    return num_sum


# Return the number of times String substring appears in String s
def substring_count(s, substring):
    count = 0

    # Longer way
    for i in range(len(s)):
        if s[i : (i + len(substring))] == substring:
            count += 1

    return count

    # Shorter way--count only works for non-overlapping matches
    #return s.count(substring)


# Return the number of words in Strings that end with String substring
# You can assume there are no punctuation marks between words
def words_ends_with_substring(s, substring):
    words = s.split(' ')
    return len([word for word in words if word.endswith(substring)])


# Given String s, return the number of characters between the first occurrence
# of String substring and the final occurrence
# You can assume that substring will appear at least twice
def distance(s, substring):
    first = 0
    last = 0

    for i in range(len(s)):
        if s[i : i + len(substring)] == substring:
            first = i + len(substring)
            break

    last_index = len(s) - len(substring) + 1
    for i in range(last_index):
        if s[last_index - i : last_index - i + len(substring)] == substring:
            last = last_index - i
            break

    return last - first

    # Shorter way
    #first = s.find(substring) + len(substring)
    #last = s.rfind(substring)
    #return last - first


# Return true if String s is a palindrome
# palindromes are words or phrases are read the same forward as backward.
# HINT: ignore/remove all punctuation and spaces in the String
def palindrome(s):
    new_str = str()

    for char in s:
        if char.isalpha():
            new_str += char.lower()

    for i in range(len(new_str)):
        if new_str[i] != new_str[len(new_str) - 1 - i]:
            return False

    return True


if __name__ == '__main__':
    words_ends_with_substring("He quietly and slowly backed away from the bear that was hungrily looking at him", "ly")
