import string

def test_len_of_strings(random_string):
    assert len(random_string) == 10


def test_reversing(random_string):
    rev_str1 = "drowasss"
    assert random_string[::-1] == rev_str1


def test_zero_devide(random_number):
    try:
        random_number/0
    except ZeroDivisionError as zd:
        assert type(zd).__name__ == 'ZeroDivisionError'


class TestLists:

    def test_search_in_list(self):
        l = [l for l in 'word' if l in string.ascii_lowercase]
        assert 'w' in l
        assert 'o' in l

    def tes_revercing(self):
        pass