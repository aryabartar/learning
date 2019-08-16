from nose.tools import assert_equal


def uni_char(string):
    s = set(string)

    if len(s) == len(string):
        return True
    return False


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print
        'ALL TEST CASES PASSED'


# Run Tests
t = TestUnique()
t.test(uni_char)
