class Tree(object):

    def __init__(self, value):
        self.value = value
        self.right_node = None
        self.left_node = None

    def __str__(self):
        return "<node with value: {}>".format(self.value)


def print_node(node):
    if node is None:
        return []

    print(node.value, end=" ")

    if node.left_node is not None and node.right_node is None:
        return (node.left_node,)

    if node.left_node is None and node.right_node is not None:
        return (node.right_node,)

    if node.left_node is None and node.right_node is None:
        return []

    return (node.left_node, node.right_node)


def print_level(node):
    array = [node]

    while len(array) != 0 and array is not None:
        temp_array = []
        for n in array:
            temp_array.extend(list(print_node(n)))
        print()
        array = temp_array


root = Tree(12)
left = Tree(5)
right = Tree(14)
left_left = Tree(1)
left_right = Tree(68)
root.left_node = left
root.right_node = right
right.right_node = Tree(99)
left.left_node = left_left
left.right_node = left_right

print_level(root)
