TEST_STRING = 'they mostly come at night. Mostly.'


def sort_word_excl_dupes(s):
    return ''.join(sorted(set(s)))

assert sort_word_excl_dupes(TEST_STRING) == ' .Maceghilmnosty'
assert sort_word_excl_dupes('') == ''
print("sort_word_excl_dupes successful!")


def reverse_sentence(s):
    return s.split(' ')[::-1] if s else []

assert reverse_sentence(TEST_STRING) == ['Mostly.', 'night.', 'at', 'come', 'mostly', 'they']
assert reverse_sentence('') == []
print("reverse_sentence successful!")
