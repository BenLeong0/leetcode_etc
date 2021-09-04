TEST_STRING = 'they mostly come at night. Mostly.'


def sort_word_excl_dupes(s):
    return ''.join(sorted(set(s)))


def test_sort_word_excl_dupes():
    assert sort_word_excl_dupes(TEST_STRING) == ' .Maceghilmnosty'
    assert sort_word_excl_dupes('') == ''

test_sort_word_excl_dupes()


def reverse_sentence(s):
    return s.split(' ')[::-1] if s else []


def test_reverse_sentence():
    assert reverse_sentence(TEST_STRING) == ['Mostly.', 'night.', 'at', 'come', 'mostly', 'they']
    assert reverse_sentence('') == []

test_reverse_sentence()
