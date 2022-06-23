"""
With this string:
'they mostly come at night. Mostly.'

1) Write a function that returns a sorted string with no duplicate characters
(keep any whitespace and punctuation):
Example: ' .Maceghilmnosty'

2) Write a function that returns the words in reverse order:
Example: ['Mostly.', 'night.', 'at', 'come', 'mostly', 'they']
"""

TEST_STRING = 'they mostly come at night. Mostly.'


def sort_word_excl_dupes(s: str):
    return ''.join(sorted(set(s)))

assert sort_word_excl_dupes(TEST_STRING) == ' .Maceghilmnosty'
assert sort_word_excl_dupes('') == ''
print("sort_word_excl_dupes successful!")


def reverse_sentence(s: str):
    return s.split(' ')[::-1] if s else []

assert reverse_sentence(TEST_STRING) == ['Mostly.', 'night.', 'at', 'come', 'mostly', 'they']
assert reverse_sentence('') == []
print("reverse_sentence successful!")
