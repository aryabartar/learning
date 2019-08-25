class Node(object):
    def __init__(self, key, value, parent=None, left_child=None, right_child=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return "<{} node>".format(self.key)


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        node = Node(key, value)

        if self.root is None:
            self.root = node

        else:
            self._insert(self.root, node)

    def _insert(self, parent, node):

        if node.key < parent.key:
            if parent.left_child is None:
                node.parent = parent
                parent.left_child = node
                return

            self._insert(parent.left_child, node)

        else:
            if parent.right_child is None:
                node.parent = parent
                parent.right_child = node

                return

            self._insert(parent.right_child, node)


def print_tree(node):
    if node is None:
        return

    print_tree(node.left_child)
    print(node.key)
    print_tree(node.right_child)


b = BinarySearchTree()
b.insert(1, 20)
b.insert(-2, 20)
b.insert(3, 20)
b.insert(2, 20)
b.insert(-10, 20)
b.insert(-1, 20)
print_tree(b.root)
