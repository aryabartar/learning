from nose.tools import assert_equal


class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def cycle_check(first_node):
    slow = first_node
    fast = first_node

    while fast.nextnode is not None:
        fast = fast.nextnode
        if fast is None:
            return False
        fast = fast.nextnode

        slow = slow.nextnode

        if slow == fast:
            return True

    return False


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a  # Cycle Here!

# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


class TestCycleCheck(object):

    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)

        print("ALL TEST CASES PASSED")


# Run Tests

t = TestCycleCheck()
t.test(cycle_check)
