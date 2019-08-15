from nose.tools import assert_equal


def large_count_sum(arr):
    c_sum = 0
    max_sum = 0

    for i in range(0, len(arr)):
        if arr[i] + c_sum > 0:
            c_sum += arr[i]
        else:
            c_sum = 0

        max_sum = max(c_sum, max_sum)

    return max_sum


class LargeContTest(object):
    def test(self, sol):
        assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(sol([-1, 1]), 1)
        print('ALL TEST CASES PASSED')


# Run Test
t = LargeContTest()
t.test(large_count_sum)
