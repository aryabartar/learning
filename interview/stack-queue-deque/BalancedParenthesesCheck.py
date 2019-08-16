from nose.tools import assert_equal


class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def balance_check(string):
    array = list(string)
    s = Stack()

    for i in array:
        if i == '(' or i == '{' or i == '[':
            s.push(i)
        else:
            popped_value = s.pop()
            if i == ')' and popped_value != '(':
                return False
            elif i == '}' and popped_value != '{':
                return False
            elif i == ']' and popped_value != '[':
                return False
    if not s.isEmpty():
        return False
    return True


class TestBalanceCheck(object):

    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print("PASSED")


# Run Tests

t = TestBalanceCheck()
t.test(balance_check)
