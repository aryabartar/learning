from nose.tools import assert_equal


def rev_word(sentence):
    sentence_split = sentence.split(" ")
    new_sentence = ""

    for word in reversed(sentence_split):
        if word == "":
            continue

        if new_sentence != "":
            new_sentence = new_sentence + " "

        new_sentence = new_sentence + word

    return new_sentence


class ReversalTest(object):

    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John    how are you   '), 'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")


# Run and test
t = ReversalTest()
t.test(rev_word)
