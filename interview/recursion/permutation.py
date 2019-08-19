from nose.tools import assert_equal


class TestPerm(object):

    def test(self, solution):
        assert_equal(sorted(solution('abc')), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')), sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))

        print('All test cases passed.')


def permute(string):
    output = []
    first_letter = string[0]

    if len(string) <= 1:
        return [string]

    string = string[1:]
    result = permute(string)

    for element in result:
        output.append(first_letter + element)
        output.append(element + first_letter)

        for i in range(1, len(element)):
            output.append(element[0:i] + first_letter + element[i:])

    return output


# Run Tests
t = TestPerm()
t.test(permute)
