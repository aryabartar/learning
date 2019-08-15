from nose.tools import assert_equal


def compress(string):
    new_str = ""

    last_char = None
    last_char_count = 0

    for c in string:

        if c != last_char:

            if last_char is not None:
                new_str = new_str + last_char
                new_str = new_str + str(last_char_count)

            last_char = c
            last_char_count = 1

        else:
            last_char += 1

    return new_str

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')


# Run Tests
t = TestCompress()
t.test(compress)
