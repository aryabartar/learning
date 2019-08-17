from nose.tools import assert_equal


class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def nth_to_last_node(nth, head):
    node = head
    for i in range(nth):
        node = node.nextnode

    back_node = head
    while node is not None:
        node = node.nextnode
        back_node = back_node.nextnode

    return back_node


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e


####

class TestNLast(object):

    def test(self, sol):
        assert_equal(sol(2, a), d)
        print('OK')


# Run tests
t = TestNLast()
t.test(nth_to_last_node)
