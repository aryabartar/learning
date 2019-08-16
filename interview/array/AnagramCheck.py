from nose.tools import assert_equal


def anagram_check(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    chars_count_dict = {}

    for c in s1:
        if c in chars_count_dict:
            chars_count_dict[c] += 1
        else:
            chars_count_dict[c] = 1

    for c in s2:
        if c in chars_count_dict:
            chars_count_dict[c] -= 1
        else:
            return False

    for c in chars_count_dict:
        if chars_count_dict[c] != 0:
            return False

    return True


class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print('ALL TEST CASES PASSED')


# Run Tests
t = AnagramTest()
t.test(anagram_check)
