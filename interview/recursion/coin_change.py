def coin_change(n, coins):
    coins = list(coins)

    if n == 0:
        return 0

    if len(coins) == 0:
        return None

    max_coin = coins.pop(-1)
    max_coin_numbers = int(n / max_coin)

    min_value = None

    for i in range(0, max_coin_numbers + 1):
        sub_coins = coin_change(n - i * max_coin, list(coins))

        if sub_coins is None:
            continue

        coins_needed = i + sub_coins

        if min_value is None or coins_needed < min_value:
            min_value = coins_needed

    return min_value


from nose.tools import assert_equal


class TestCoins(object):

    def check(self, solution):
        coins = [1, 5, 10, 25]
        assert_equal(solution(45, coins), 3)
        assert_equal(solution(23, coins), 5)
        assert_equal(solution(74, coins), 8)
        print('Passed all tests.')


# Run Test

test = TestCoins()
test.check(coin_change)

# print(coin_change(74, [1, 5, 10, 25]))
