def find_missing_element(arr1, arr2):
    dict = {}

    for i in arr1:
        element = dict.get(i)
        if element:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in arr2:
        dict[i] -= 1

    for (k, v) in dict.items():
        if v == 1:
            return k


from nose.tools import assert_equal


class TestFinder(object):

    def test(self, sol):
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print('ALL TEST CASES PASSED')


# Run test
t = TestFinder()
t.test(find_missing_element)
